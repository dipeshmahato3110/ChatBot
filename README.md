# ChatBot with AI-based Auto Response using Google Gemini API

This project is a smart WhatsApp automation bot that reads incoming messages, detects the sender's language style (Hinglish, Bengali mix, or English), and replies naturally using Google's Gemini Pro 2.5 model.

## 🔍 Features

- ✅ Detects new messages from the sender
- 🌐 Automatically generates context-aware replies using Google Gemini
- 📋 Copies and pastes responses into WhatsApp
- 🔁 Runs in a continuous loop and avoids duplicate replies
- 💬 Mimics human tone and informal chat style

## 🧠 Tech Stack

- 🐍 Python
- 🖱️ PyAutoGUI
- 📋 Pyperclip
- 🧠 Google Generative AI (Gemini API)

## ⚙️ How It Works

1. Selects WhatsApp message area
2. Detects new messages from the sender
3. Sends the latest message to Gemini for response
4. Copies the generated reply
5. Pastes and sends it back in WhatsApp automatically

## 📦 Requirements

- Python 3.10+
- Google Generative AI SDK (`google-generativeai`)
- `pyautogui`
- `pyperclip`
- A valid Gemini API key

Install with:
```bash
pip install google-generativeai pyautogui pyperclip

