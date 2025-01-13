import streamlit as st
import pandas as pd
import datetime

# Title of the app
st.title("Prototype for Major and Minor Depression and Early Treatment")

# Depression Screening - PHQ-9
st.header("Depression Screening Questionnaire (PHQ-9)")

questions_depression = [
    "Little interest or pleasure in doing things?",
    "Feeling down, depressed, or hopeless?",
    "Trouble falling or staying asleep, or sleeping too much?",
    "Feeling tired or having little energy?",
    "Poor appetite or overeating?",
    "Feeling bad about yourself, or that you are a failure or have let yourself or your family down?",
    "Trouble concentrating on things, such as reading the newspaper or watching television?",
    "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual?",
    "Thoughts that you would be better off dead, or of hurting yourself in some way?"
]

responses_depression = []
for question in questions_depression:
    response = st.radio(question, ['Not at all', 'Several days', 'More than half the days', 'Nearly every day'])
    responses_depression.append(response)

response_mapping = {
    'Not at all': 0,
    'Several days': 1,
    'More than half the days': 2,
    'Nearly every day': 3
}

score_depression = sum([response_mapping[response] for response in responses_depression])

# Feedback based on depression score
if score_depression < 5:
    st.write("Your depression severity is **minor**. Consider practicing self-care, exercise, and socializing to improve your mood.")
elif score_depression >= 5:
    st.write("You may be experiencing **major depression**. It's strongly recommended to consult with a healthcare provider for personalized treatment.")

# Mood Tracker (Simple Version)
st.header("Track Your Mood")

mood = st.radio("How do you feel today?", ["Happy", "Neutral", "Sad", "Angry", "Anxious"])
mood_log = st.button("Log Mood")
if mood_log:
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    st.write(f"Your mood on {date}: {mood}")
    # Here you can store the mood log into a file or database if needed

# Self-Care Tips Based on Severity
st.header("Self-Care Tips")
if score_depression < 5:
    st.write("Try incorporating regular physical exercise, staying connected with friends and family, and maintaining a healthy routine.")
else:
    st.write("Consider seeking therapy, trying medication, or engaging in support groups for better management of symptoms.")

# Emergency Help Button
st.header("Need Immediate Help?")
if st.button("Emergency Help"):
    st.write("[Click here for National Suicide Prevention Lifeline](https://suicidepreventionlifeline.org/)")

# Journal Section
st.header("Personal Journal")
journal_entry = st.text_area("Write down your thoughts or feelings:")
if journal_entry:
    st.write("Your journal entry has been recorded. Keep track of your emotional state over time.")

# Resources for Support
st.subheader("Resources for Support")
st.write("[Malaysian Mental Health Association](https://mmha.org.my)")


