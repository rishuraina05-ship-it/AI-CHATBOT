import streamlit as st

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("AI Chatbot 🤖")

# store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# user input
user_input = st.chat_input("Type your message...")

if user_input:
    # user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # simple AI reply logic
    if "hello" in user_input.lower():
        reply = "Hello! How can I help you?"
    elif "job" in user_input.lower():
        reply = "Keep applying and building projects. You're on the right track!"
    elif "python" in user_input.lower():
        reply = "Python is great for AI, data analysis, and automation."
    else:
        reply = "I'm still learning, but I can help with AI, jobs, and coding basics!"

    # AI response
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)