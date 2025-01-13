import streamlit as st
import pandas as pd
import datetime

# Title of the app
st.title("Prototype for Major and Minor Depression and Early Treatment")
st.write("This prototype aims to provide a self-assessment and educational tool for understanding mental health,focusing on depression and anxiety.It also offers personalized feedback, mood tracking, self-care suggestions, journaling, and access to resources for further support.")

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

# Depression feedback
if score_depression < 5:
    st.write("Your depression severity is **minor**. Consider practicing self-care, exercise, and socializing to improve your mood.")
elif score_depression >= 5:
    st.write("You may be experiencing **major depression**. It's strongly recommended to consult with a healthcare provider for personalized treatment.")

# Anxiety Screening - GAD-7
st.header("Anxiety Screening Questionnaire (GAD-7)")
questions_anxiety = [
    "Feeling nervous, anxious, or on edge?",
    "Not being able to stop or control worrying?",
    "Worrying too much about different things?",
    "Trouble relaxing?",
    "Being so restless that it's hard to sit still?",
    "Becoming easily annoyed or irritable?",
    "Feeling afraid as if something awful might happen?"
]
responses_anxiety = []
for question in questions_anxiety:
    response = st.radio(question, ['Not at all', 'Several days', 'More than half the days', 'Nearly every day'])
    responses_anxiety.append(response)

score_anxiety = sum([response_mapping[response] for response in responses_anxiety])

# Anxiety feedback
if score_anxiety < 14:
    st.write("Your anxiety severity is **minor**. Maintain healthy habits to keep anxiety levels low.")
else:
    st.write("You may have **severe anxiety**. It's important to consult a healthcare professional for tailored treatment.")

# Mood Tracker
st.header("Track Your Mood")
mood = st.radio("How do you feel today?", ["Happy", "Neutral", "Sad", "Angry", "Anxious"])
mood_log = st.button("Log Mood")
if mood_log:
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    st.write(f"Your mood on {date}: {mood}")
    
# Activity Recommendation Based on Mood
st.header("Activity Recommendations Based On Mood")
if mood == "Happy":
    st.write("Great! How about sharing your happiness by calling a friend or volunteering?")
elif mood == "Neutral":
    st.write("Consider doing something you enjoy, like a hobby or a short walk, to uplift your day.")
elif mood == "Sad":
    st.write("Try listening to your favorite music, taking a nature walk, or talking to someone you trust.")
elif mood == "Angry":
    st.write("Consider calming activities like deep breathing exercises, meditation, or a physical workout.")
elif mood == "Anxious":
    st.write("Try guided meditation or a grounding exercise to calm your mind.")


# Self-Care Tips
st.header("Self-Care Tips")
if score_depression < 5 and score_anxiety < 5:
    st.write("Try incorporating regular physical exercise, staying connected with friends and family, and maintaining a healthy routine.")
else:
    st.write("Consider seeking therapy, trying medication, or engaging in support groups for better management of symptoms.")

# Daily Habit Tracker 
st.header("Daily Habit Tracker")
habits = st.multiselect("Select completed habits today:", ["Drank 8 glasses of water", "Exercised", "Took medication", "Read a book", "Meditated"])
if st.button("Log Habits"):
    st.write(f"Habits logged for today: {', '.join(habits)}")
    # Store habits for persistence


# Emergency Help Button
st.header("Need Immediate Help?")
if st.button("Emergency Help"):
    st.write("[Click here for Malaysia Suicide Prevention Lifeline](https://findahelpline.com/countries/my/topics/suicidal-thoughts)")

# Journal Section
st.header("Personal Journal")
journal_entry = st.text_area("Write down your thoughts or feelings:")
if journal_entry:
    st.write("Your journal entry has been recorded. Keep track of your emotional state over time.")
    # Implement data persistence for journal entries if needed

# Resources for Support
st.subheader("Resources for Support")
if st.button("Resources"):
    st.write("[Malaysian Mental Health Association](https://mmha.org.my)")
    st.write("[National Alliance on Mental Illness (NAMI)](https://www.nami.org)")
    st.write("[BetterHelp - Online Counseling](https://www.betterhelp.com)")