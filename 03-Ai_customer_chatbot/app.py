import streamlit as st

from src.chatbot import ChatBot


# Load chatbot
bot = ChatBot()

# Page configuration
st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Customer Support Chatbot")

st.write("Ask me anything about our services.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot Response
    response = bot.chat(user_input)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)

# Clear Chat Button
if st.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()