import streamlit as st
from chatbot_core import handle_user_input

st.set_page_config(page_title="Amani – Your Mental Health Companion", layout="centered")

st.title("🧠 Amani – Your Mental Health Companion")
st.markdown(
    """
    Welcome to **Amani**, your supportive AI therapist.  
    Share your thoughts or feelings, and I’ll do my best to guide you.  
    _(Please note: This tool is not a substitute for professional help.)_
    """
)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'disorder' not in st.session_state:
    st.session_state.disorder = None
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'demographics' not in st.session_state:
    st.session_state.demographics = {}

# Collect demographics once
if not st.session_state.demographics:
    with st.form("demographics_form"):
        st.subheader("🧍 Tell me a bit about yourself")
        age = st.number_input("Age", min_value=5, max_value=100, step=1)
        gender = st.selectbox("Gender", ["Prefer not to say", "Male", "Female", "Other"])
        occupation = st.text_input("Occupation")
        stress_level = st.slider("Stress level (1 = Low, 10 = High)", 1, 10, 5)
        submitted = st.form_submit_button("Start Chat")

        if submitted:
            st.session_state.demographics = {
                "age": age,
                "gender": gender,
                "occupation": occupation,
                "stress_level": stress_level
            }
            st.rerun()

# Display chat history
for msg in st.session_state.messages:
    role = "user" if msg["role"] == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(msg["content"])

# Handle user input
user_input = st.chat_input("How are you feeling today?")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response, disorder, next_index = handle_user_input(
        user_input,
        st.session_state.demographics,
        st.session_state.disorder,
        st.session_state.question_index
    )

    st.session_state.disorder = disorder
    st.session_state.question_index = next_index
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
