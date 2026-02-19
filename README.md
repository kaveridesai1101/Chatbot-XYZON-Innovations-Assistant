# 🤖 XYZON Innovations Assistant - AI Support Chatbot

An intelligent, responsive conversation system designed for website user support. This chatbot specializes in providing guidance on internships, courses, Learning Management System (LMS) support, and professional resume building.

## 🌟 Key Features

- **🎯 Intelligent Intent Discovery**: Identifies user needs (Internships, Courses, LMS, Resume Builder) using precise regex-based classification.
- **💬 Proactive Engagement**: Automatic welcome popup on website load for immediate assistance.
- **📚 Deep Knowledge Base**: Over 200 lines of curated FAQ data for instant, accurate responses.
- **🛡️ Robust Stability**: Implements safe dictionary lookups and fallback logic to ensure continuous availability.
- **🎨 Premium UI/UX**: Professional dark-themed interface with smooth animations and responsive design.

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python), Uvicorn, Pydantic
- **Frontend**: Vanilla JavaScript, CSS3 (Flexbox/Animations), HTML5
- **Logic**: Regex-based Intent Classifier, Response Generator with Context Awareness

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8+
- Modern Web Browser (Chrome, Edge, etc.)

### 2. Backend Setup
```bash
# Navigate to the project directory
cd Chatbot

# Install dependencies (if not already present)
pip install fastapi uvicorn pydantic

# Run the server
python backend/main.py
```
*The server will start at `http://localhost:8000`*

### 3. Frontend Setup
Simply open `index.html` in your browser to start interacting with the assistant.

## 📂 Project Structure

```text
Chatbot/
├── backend/
│   ├── main.py               # FastAPI entry point
│   ├── response_generator.py # Intent classification engine
│   └── knowledge_base.py     # Curated support data
├── frontend/
│   ├── chatbot.js            # Frontend logic & API integration
│   └── chatbot.css           # Styling & Animations
├── index.html                # Main landing page
└── README.md                 # Project documentation
```

## 👨‍💻 Author
**Kaveri Desai**

---
*Developed for the Generative AI Internship Evaluation at XYZON Innovations.*
