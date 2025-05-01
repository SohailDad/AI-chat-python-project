
import streamlit as st


def gemini_model(user_input):
    pass


# Initialize session state for storing user inputs
if "user_inputs" not in st.session_state:
    st.session_state.user_inputs = []

# Input from user
with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input("Type your message", placeholder="Say something...", label_visibility="collapsed")
    with col2:
        submitted = st.form_submit_button("Send")

    # Add input to session state if submitted
    if submitted and user_input:
        gemini_model(user_input)
        st.session_state.user_inputs.append(user_input)

# Display all inputs dynamically
if st.session_state.user_inputs:
    st.markdown("### Messages:")
    st.markdown("\n".join([f"- **User:** {message}" for message in st.session_state.user_inputs]))

    


    