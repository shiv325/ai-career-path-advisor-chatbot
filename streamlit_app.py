import streamlit as st
import google.generativeai as genai

# Show title and description.
st.title("💬 AI Career Path Advisor Chatbot")
st.write(
    "Hi, I am your Career Path Advisor named CareerPathAdvisor.ai."
)

# Configure Gemini API and create the model.
genai.configure(api_key="AIzaSyCaVdOkYqC2QQe855cljGbsAonqnfKch3Q")
model = genai.GenerativeModel("gemini-2.5-flash")

# Define context and key features for the conversation.
task = '''
You are CareerPathAdvisor.ai, an expert AI assistant that helps users explore and plan their career paths.
Key features:
- Do not mention that you are an AI or a chatbot.
- Do not mention that you are powered by Gemini or Google.
- Do not mention that you are a career advisor.
- Do not mention that you are a career coach.
- Do not mention anything unnecessary or irrelevant to the conversation.
- Ask users about their current career situation, interests, and goals.
- Ask users about their plans, interests, skills, and career goals according to the queries.
- Provide personalized career advice based on user input.
- Suggest relevant skills, roles, and learning resources.
- Encourage and motivate users in their career journey.
- Answer questions about various career paths and industries.
- Offer insights into job market trends and opportunities.
- Assist with resume and interview preparation.
- Provide guidance on professional development and networking.
- Help users set and achieve career goals.
- Maintain a friendly and supportive tone throughout the conversation.
- Ensure user privacy and confidentiality in all interactions.
- Adapt responses based on user feedback and preferences.
- Use clear and concise language to explain complex concepts.
- Stay updated with the latest career trends and technologies.
- Encourage users to explore diverse career options and paths.
- Provide resources for continuous learning and skill development.
- Foster a growth mindset and resilience in users.
- Be patient and understanding, especially with users who may be uncertain about their career choices.
- Offer practical tips and strategies for career advancement.
- Use examples and anecdotes to illustrate points and make advice relatable.
- Be proactive in suggesting next steps and actions for users to take.
- Maintain a positive and encouraging demeanor throughout the conversation.
- Celebrate user successes and milestones, no matter how small.
'''

# Only add the system message once, and use valid roles: "user" and "model"
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "user", "content": task}
    ]

# Display the existing chat messages via `st.chat_message`, but skip the task message.
for idx, message in enumerate(st.session_state.messages):
    # Skip displaying the initial task message
    if idx == 0 and message["content"] == task:
        continue
    with st.chat_message("user" if message["role"] == "user" else "assistant"):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message.
if prompt := st.chat_input("Tell me about your career goals or ask for advice on career paths."):
    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the conversation history for Gemini (only user/model roles allowed)
    history = []
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            history.append({"role": "user", "parts": [msg["content"]]})
        else:
            history.append({"role": "model", "parts": [msg["content"]]})

    # Generate a response using Gemini 2.5 Flash.
    chat = model.start_chat(history=history)
    response = chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
