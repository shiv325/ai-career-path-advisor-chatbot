import streamlit as st
import google.generativeai as genai

# Show title and description.
st.title("💬 AI Career Path Advisor Chatbot")
st.write(
    "Hi, I am your Career Path Advisor named CareerPathAdvisor.ai. "
    "This app uses Gemini 2.5 Flash for career advice."
)

# Create a Gemini client and chat session.
genai.configure(api_key="AIzaSyCaVdOkYqC2QQe855cljGbsAonqnfKch3Q")
model = genai.GenerativeModel("gemini-2.5-flash")
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Create a session state variable to store the chat messages.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message.
if prompt := st.chat_input("What is up?"):

    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a response using Gemini 2.5 Flash.
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
