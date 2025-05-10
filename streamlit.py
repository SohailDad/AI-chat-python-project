import streamlit as st
import model 




# Initialize session state for storing user inputs
if "user_inputs" not in st.session_state:
    st.session_state.user_inputs = []
    st.session_state.model_output = []

# Input from user
with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input("Type your message", placeholder="Say something...", label_visibility="collapsed")
    with col2:
        submitted = st.form_submit_button("Send")

    # Add input to session state if submitted
    if submitted and user_input:
        model_output = model.gemini_model(user_input)
        st.session_state.user_inputs.append(user_input)
        st.session_state.model_output.append(model_output)

# Display all inputs dynamically
if st.session_state.user_inputs:
    st.markdown("### Messages:")
    col1, col2 = st.columns([5, 5])
    with col1:
        st.markdown("### User:")
        st.markdown("\n".join([f"- **User:** {message}" for message in st.session_state.user_inputs[::-1]]))
    with col2:
        st.markdown("### Model Reply:")
        st.markdown("\n".join([f"- **Model:** {message}" for message in st.session_state.model_output[::-1]]))
       
    


    