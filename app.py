import streamlit as st
from langchain_ai import extract_study_information
from fuzzy_logic import calculate_study_priority


# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="AI Study Priority System",
    page_icon="📚",
    layout="centered"
)


# -----------------------------------
# Title
# -----------------------------------
st.title("📚 AI-Based Student Study Priority Recommendation System")

st.write(
    "Enter your study situation in simple English. "
    "AI will extract the study information and Fuzzy Logic "
    "will calculate your study priority."
)


# -----------------------------------
# Student Input
# -----------------------------------
student_input = st.text_area(
    "📝 Describe your study situation",
    placeholder=(
        "Example: My Data Mining exam is in 3 days. "
        "I have completed 40% of the syllabus. "
        "The subject is difficult and 2 chapters are pending."
    ),
    height=150
)


# -----------------------------------
# Analyze Button
# -----------------------------------
if st.button("🔍 Analyze Study Situation"):

    if not student_input.strip():

        st.warning("⚠️ Please enter your study situation first.")

    else:

        try:

            # -----------------------------------
            # Step 1: AI / LangChain Extraction
            # -----------------------------------
            with st.spinner("🤖 AI is understanding your study situation..."):

                extracted_info = extract_study_information(
                    student_input
                )

            st.success("✅ AI analysis completed!")


            # -----------------------------------
            # Step 2: Display AI Information
            # -----------------------------------
            st.subheader("📊 AI Extracted Information")

            col1, col2 = st.columns(2)

            with col1:

                st.write("**📚 Subject**")
                st.info(extracted_info["subject"])

                st.write("**⏳ Days Left**")
                st.info(
                    str(extracted_info["days_left"])
                )

                st.write("**📖 Preparation**")
                st.info(
                    str(extracted_info["preparation"]) + "%"
                )

            with col2:

                st.write("**⚡ Difficulty**")
                st.info(
                    str(extracted_info["difficulty"]) + "/10"
                )

                st.write("**📕 Pending Chapters**")
                st.info(
                    str(extracted_info["pending_chapters"])
                )


            # -----------------------------------
            # Step 3: Fuzzy Logic
            # -----------------------------------
            with st.spinner("🧠 Fuzzy Logic is calculating priority..."):

                score, category = calculate_study_priority(
                    extracted_info["days_left"],
                    extracted_info["preparation"],
                    extracted_info["difficulty"],
                    extracted_info["pending_chapters"]
                )


            # -----------------------------------
            # Step 4: Fuzzy Result
            # -----------------------------------
            st.divider()

            st.subheader("🧠 Fuzzy Logic Result")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Priority Score",
                    f"{score:.2f} / 100"
                )

            with col2:

                st.metric(
                    "Study Priority",
                    category
                )


            # -----------------------------------
            # Step 5: Recommendation
            # -----------------------------------

            st.subheader("💡 Study Recommendation")

            if category == "High Priority":

                recommendation = (
                    f"Your {extracted_info['subject']} preparation "
                    f"requires immediate attention. You have only "
                    f"{extracted_info['days_left']} days left and "
                    f"{extracted_info['preparation']}% of the syllabus "
                    f"is completed. Focus on the pending chapters first "
                    f"and revise important topics regularly."
                )

            elif category == "Medium Priority":

                recommendation = (
                    f"Your {extracted_info['subject']} preparation "
                    f"needs regular attention. Continue studying "
                    f"consistently, complete the pending chapters, "
                    f"and revise the topics you have already covered."
                )

            else:

                recommendation = (
                    f"Your {extracted_info['subject']} preparation "
                    f"is currently at a lower priority. Maintain your "
                    f"study schedule and use the available time for "
                    f"revision and practice."
                )

            st.success(recommendation)


            # -----------------------------------
            # Step 6: System Explanation
            # -----------------------------------

            st.divider()

            st.subheader("⚙️ How the System Works")

            st.write(
                "1️⃣ **LangChain + Gemini:** Understands the "
                "student's natural-language study situation."
            )

            st.write(
                "2️⃣ **Information Extraction:** Extracts subject, "
                "days left, preparation, difficulty and pending chapters."
            )

            st.write(
                "3️⃣ **Fuzzy Logic:** Applies membership functions "
                "and fuzzy rules to calculate the priority."
            )

            st.write(
                "4️⃣ **Defuzzification:** Converts the fuzzy result "
                "into a numerical priority score from 0 to 100."
            )

            st.write(
                "5️⃣ **Recommendation:** Provides a study recommendation "
                "based on the calculated priority."
            )


        except Exception as e:

            st.error(
                "❌ An error occurred while analyzing your study situation."
            )

            st.code(str(e))