import json
import re
from langchain_google_genai import ChatGoogleGenerativeAI


def extract_study_information(student_input):

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0
    )

    prompt = f"""
You are a student study-planning assistant.

Read the student's situation and extract these 5 values:

1. subject
2. days_left
3. preparation
4. difficulty
5. pending_chapters

Return ONLY valid JSON.
Do not use markdown.
Do not use ```.

The JSON format must be exactly:

{{
    "subject": "Data Mining",
    "days_left": 3,
    "preparation": 40,
    "difficulty": 8,
    "pending_chapters": 2
}}

Student situation:
{student_input}
"""

    response = llm.invoke(prompt)

    # Get text from LangChain response
    content = response.content

    if isinstance(content, list):
        text = ""

        for block in content:
            if isinstance(block, dict):
                if "text" in block:
                    text += block["text"]
            else:
                text += str(block)

        content = text

    content = str(content).strip()

    # Find JSON inside the response
    match = re.search(r"\{.*\}", content, re.DOTALL)

    if not match:
        raise ValueError("AI did not return valid JSON.")

    json_text = match.group(0)

    data = json.loads(json_text)

    # Clean and validate values
    subject = str(data.get("subject", "Unknown"))

    days_left = int(data.get("days_left", 0))
    preparation = int(data.get("preparation", 0))
    difficulty = int(data.get("difficulty", 5))
    pending_chapters = int(data.get("pending_chapters", 0))

    # Keep values within valid ranges
    days_left = max(0, days_left)
    preparation = max(0, min(100, preparation))
    difficulty = max(1, min(10, difficulty))
    pending_chapters = max(0, pending_chapters)

    return {
        "subject": subject,
        "days_left": days_left,
        "preparation": preparation,
        "difficulty": difficulty,
        "pending_chapters": pending_chapters
    }