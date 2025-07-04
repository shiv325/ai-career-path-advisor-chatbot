import streamlit as st
from google import genai

# Show title and description.
st.title("💬 AI Career Path Advisor Chatbot")
st.write(
    "Hi, I am your Career Path Advisor named CareerPathAdvisor.ai. "
    "This app uses Gemini 2.5 Flash for career advice."
)

# Create a Gemini client.
client = genai.Client(api_key = "AIzaSyCaVdOkYqC2QQe855cljGbsAonqnfKch3Q")
chat = client.chats.create(model = "gemini-2.5-flash")

# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.chat_input("What is up?"):

    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a response using Gemini 2.5 Flash.
    response = chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
