# 📚 AI-Based Student Study Priority Recommendation System

## 📌 Project Overview

The AI-Based Student Study Priority Recommendation System helps students identify which study situations require more attention.

The system accepts a student's study situation in natural language and uses Artificial Intelligence and Fuzzy Logic to calculate a study priority score.

## 🎯 Objectives

- Understand a student's study situation using Natural Language Processing.
- Extract important study information using LangChain and Gemini.
- Calculate study priority using a genuine Fuzzy Logic system.
- Provide a priority score from 0 to 100.
- Generate a simple study recommendation.

## 🤖 AI Component

The project uses:

- Python
- LangChain
- Google Gemini
- Streamlit

The student enters a natural-language description such as:

> My Data Mining exam is in 3 days. I have completed 40% of the syllabus. The subject is difficult and 2 chapters are pending.

The AI extracts:

- Subject
- Days left
- Preparation percentage
- Difficulty level
- Pending chapters

## 🧠 Fuzzy Logic Component

The extracted information is passed to a Fuzzy Inference System.

### Input Variables

1. Exam Urgency
2. Preparation Level
3. Subject Difficulty
4. Pending Chapters

### Output

The system produces:

- Priority Score: 0–100
- Low Priority
- Medium Priority
- High Priority

The system uses membership functions, fuzzy rules and defuzzification.

## 🔄 System Workflow

User Input

↓

LangChain + Gemini

↓

Information Extraction

↓

Fuzzification

↓

Fuzzy Rule Evaluation

↓

Defuzzification

↓

Priority Score

↓

Study Recommendation

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini
- Scikit-Fuzzy
- NumPy
- Pandas
- SciPy
- NetworkX

## 📊 Example Result

For a student with:

- Days Left: 3
- Preparation: 40%
- Difficulty: 8/10
- Pending Chapters: 2

The system calculates:

**Priority Score: 81.22 / 100**

**Priority: High Priority**

## ▶️ How to Run

Install the required packages:

```bash
pip install -r requirements.txt