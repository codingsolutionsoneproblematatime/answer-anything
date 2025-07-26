# Answer Anything - Real-Time Screen Explainer

Answer Anything is a lightweight, real-time desktop assistant that lets you highlight anything on your screen: code, graphs, documents, or UI, and get **instant, AI-powered explanations** using OpenAI’s GPT-4o Vision model.

No copy/paste. No switching tabs. No switching applications. Just **drag, ask, and get answers.**

<img width="457" height="549" alt="image" src="https://github.com/user-attachments/assets/7232bdaf-69bd-4115-b832-402248627b76" />

---

## Features

- Drag-to-select screen region
- Custom prompts ("Explain this", "Summarize this", "What is this?")
- GPT-4o Vision multimodal AI (image + text input)
- Minimal overlay UI — works over any application
- Perfect for:
  - Developers reading unfamiliar code
  - Analysts working with complex dashboards
  - Students studying problems, diagrams, or text
  - Anyone encountering confusing content on screen

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/answer-anything.git
cd answer-anything
```

### 2. Set Up the Environment
```bash
Copy
Edit
python -m venv venv
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
```

### 3. Add Your OpenAI API Key
Create a .env file in the root directory with:

```ini
Copy
Edit
OPENAI_API_KEY=sk-...
```

### 4. Run It
```bash
Copy
Edit
python real-time-screen-explainer.py
```
Then use:

Ctrl+Shift+E → to activate the region selector

Esc → to quit the background listener

### Example Prompts
“What does this Python code do?”

“Summarize this chart.”

“Explain this UI screen.”

“Translate this menu to English.”

“What is this math problem asking?”

### Why I Built This
Answer Anything is designed to bring the power of GPT-4o’s vision model directly to your screen — turning your desktop into an interactive, explorable space. It’s like adding an “Explain This” button to your operating system. My goal was to create a tool that enhances curiosity, speeds up understanding, and eliminates context-switching.

### Tech Stack
Python 3.11

tkinter — GUI overlay + prompt input

pyautogui — region screenshotting

openai — GPT-4o Vision API

keyboard — hotkey listener

dotenv — environment variable support

### Responsible Use
This project is meant to support learning, productivity, and accessibility. It is not intended for use during exams, proctored tests, or in violation of any integrity policies. Use responsibly.

### Possible Extensions
Session memory for follow-up questions

Auto-copy results to clipboard

Toolbar or tray icon support

Export answers to Markdown or notes app

OCR fallback for systems without native screenshot support
