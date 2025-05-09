import streamlit as st

# Page config
st.set_page_config(page_title="Chat App", layout="wide")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Custom CSS to fix input at bottom
st.markdown("""
    <style>
    .fixed-bottom {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f9f9f9;
        padding: 10px 20px;
        border-top: 1px solid #ddd;
        z-index: 9999;
    }
    .chat-box {
        height: 50vh;
        overflow-y: auto;
        padding: 10px;
        margin-bottom: 70px;
        border: 1px solid #ccc;
        border-radius: 10px;
        background-color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# Chat display area
st.markdown('<div class="chat-box">', unsafe_allow_html=True)
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**🧑 You:** {chat['message']}")
    else:
        st.markdown(f"**🤖 Bot:** {chat['message']}")
st.markdown('</div>', unsafe_allow_html=True)

# Fixed input form
st.markdown('<div class="fixed-bottom">', unsafe_allow_html=True)
with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input("Type your message", placeholder="Say something...", label_visibility="collapsed")
    with col2:
        submitted = st.form_submit_button("Send")

    if submitted and user_input.strip():
        # Save user message
        st.session_state.chat_history.append({"role": "user", "message": user_input})

        # Dummy bot response
        bot_reply = f"Echo: {user_input}"
        st.session_state.chat_history.append({"role": "bot", "message": bot_reply})
st.markdown('</div>', unsafe_allow_html=True)
