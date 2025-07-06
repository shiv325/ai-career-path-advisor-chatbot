# 💬 AI Career Path Advisor

A fully functional Streamlit app that helps users explore and plan their career in Artificial Intelligence. This chatbot leverages Gemini 2.5 Flash to provide personalized career advice, answer questions about AI roles, required skills, learning resources, and more.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-career-path-advisor.streamlit.app/)

---

## 🚀 Features

- **Conversational AI:** Chatbot interface powered by Gemini 2.5 Flash for natural, contextual conversations.
- **Career Guidance:** Get tailored advice on AI career paths, including roles like Data Scientist, ML Engineer, Researcher, and more.
- **Skill Gap Analysis:** Ask the bot what skills you need for a specific AI job or how to transition from your current role.
- **Learning Resources:** Get curated recommendations for courses, books, and online materials.
- **Resume & Interview Tips:** Receive suggestions for resume building and interview preparation in the AI domain.
- **Streamlit UI:** Clean, responsive web interface with persistent chat history.
- **Open Source:** Easy to customize and extend for your own use cases.

---

## 🖥️ Programming Languages & Technologies Used

- **Python 3.8+** — Main programming language for backend and app logic.
- **Streamlit** — For building the interactive web UI.
- **Google Generative AI (Gemini 2.5 Flash)** — For conversational AI and career advice.
- **python-dotenv** — For environment variable management.
- **Streamlit Secrets** — For secure API key management.
- **HTML/CSS** — For UI rendering (handled by Streamlit).
- **Git** — For version control.
- **Node.js, npm, eslint** — Pre-installed in the dev container for JavaScript development if needed.

---

## 🏗️ Project Structure

```
ai-career-path-advisor/
├── streamlit_app.py         # Main Streamlit app
├── requirements.txt         # Python dependencies
├── .streamlit/              # Streamlit config files
│   └── secrets.toml
├── README.md                # This file
└── (other supporting files)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-career-path-advisor.git
cd ai-career-path-advisor
```

### 2. Install the Requirements

Make sure you have Python 3.8+ and pip installed.

```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys

This app uses Gemini 2.5 Flash via the Google Generative AI API.  
You can set your API key in one of two ways:

- **Option 1:** Create a `.env` file in the project root and add your API key:
  ```
  GOOGLE_API_KEY=your_gemini_api_key_here
  ```
- **Option 2:** Change the value of `gemini_api_key` in `.streamlit/secrets.toml`:
  ```
  [default]
  gemini_api_key = "your_gemini_api_key_here"
  ```

> **Note:** You can get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 4. Run the App

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🌐 Run in the Browser

No installation needed!  
Try it instantly: [ai-career-path-advisor.streamlit.app](https://ai-career-path-advisor.streamlit.app/)

---

## 💡 Usage

- Type your career-related questions in the chat box.
- Example prompts:
  - "What skills do I need to become a machine learning engineer?"
  - "How do I transition from software engineering to AI research?"
  - "Suggest some beginner-friendly AI courses."
  - "What are the top companies hiring for AI roles in 2025?"
- The chatbot will respond with detailed, actionable advice.

---

## 🛠️ Customization

- **Modify prompts:** Edit `streamlit_app.py` to change the system prompt or add custom logic.
- **Add new features:** Integrate more APIs, add file upload, or connect to a database as needed.
- **UI tweaks:** Use Streamlit components to enhance the interface.

---

## 🧩 Dependencies

- [streamlit](https://streamlit.io/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- (See `requirements.txt` for the full list)

---

## 📝 License

This project is licensed under the MIT License.

---

## 🙋 FAQ

**Q:** Is my data private?  
**A:** All conversations are processed via the Gemini API. No data is stored unless you modify the code to do so.

**Q:** Can I deploy this on my own server?  
**A:** Yes! You can deploy on Streamlit Cloud, Heroku, or any cloud VM.

**Q:** Can I use a different LLM?  
**A:** Yes, with minor code changes you can swap Gemini for OpenAI, Anthropic, etc.

---

## 🔮 Future Scope & Improvements

- **Multi-LLM Support:** Enable seamless switching between Gemini, OpenAI, Anthropic, and other LLM providers.
- **User Authentication:** Allow users to create accounts and save chat history or personalized career plans.
- **Advanced Skill Gap Analysis:** Integrate with LinkedIn or allow resume uploads for automated skill extraction and gap analysis.
- **Job Board Integration:** Display live AI job postings from popular job boards.
- **Personalized Roadmaps:** Generate step-by-step learning or career roadmaps based on user background and goals.
- **Resource Ratings:** Let users rate and review recommended courses and resources.
- **Notifications & Reminders:** Email or in-app reminders for learning goals or new job postings.
- **Mobile App:** Build a companion mobile app for on-the-go career advice.
- **Localization:** Support multiple languages and regional AI job market insights.
- **Community Forum:** Add a discussion board for users to share experiences and advice.
- **Analytics Dashboard:** Visualize user progress, skill acquisition, and market trends.
- **Voice Assistant Integration:** Enable voice-based queries and responses.

Contributions and suggestions for new features are always welcome!

---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
Please open an issue to discuss your ideas or report bugs.

---

## 📫 Contact

For questions or support, open an issue or contact [kshivam@tuta.io](mailto:kshivam@tuta.io)
