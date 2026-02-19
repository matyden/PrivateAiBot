# PrivateAiBot — your simple AI solution

---

### 🤖 Simple Telegram AI Assistant

> 🚀 Want to build your own AI agent in Telegram in minutes?  
> This project is your simple, clean, and practical starting point.

A lightweight Telegram AI bot built with **aiogram** and powered by **Google Gemini (gemini-3-flash)**.  
Minimal setup. Clean architecture. Easy to extend.

This project is perfect if you:
- Want to learn how Telegram bots work
- Want to integrate an LLM into your own project
- Need a private AI assistant for a limited group of users
- Prefer clean and understandable code over complex frameworks

---

## ✨ Features

- 🔐 Whitelisted users (private bot access)
- 💬 Text-based AI responses
- ⚡ Powered by Gemini 3 Flash
- 🧠 Easy to extend with context memory
- 🛠 Built with modern `aiogram` (v3+ style)

---

## 🧱 Tech Stack

- Python 3.10+
- aiogram
- Google Generative AI SDK
- Telegram Bot API
- Gemini 3 Flash model via Google AI Studio

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / Mac**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

If you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a configuration file `.env`

You need:

- `BOT_TOKEN` – from Telegram BotFather
- `AI_TOKEN` – from Google AI Studio
- `ALLOWED_USERS` – list of Telegram user IDs allowed to use the bot

Example `.env`:

```
BOT_TOKEN=your_telegram_bot_token
AI_TOKEN=your_gemini_api_key
ALLOWED_USERS=[123456789, 987654321, 147852369]
```

The `config_reader.py` is already configured.

---

## ▶️ Run the bot

```bash
python bot.py
```

If everything is correct, your bot will start polling and be ready to receive messages.

---

## 🧠 How It Works

1. User sends a message.
2. Bot checks if the user is allowed.
3. The message is sent to Gemini (`gemini-3-flash-preview`).
4. The AI response is returned back to the user.

Minimal logic. Maximum clarity.

---

## 🔑 How to Get Gemini API Key?

1. Go here https://aistudio.google.com/api-keys
2. Create new key 
3. Copy it and paste into `.env`

## 📌 Available Commands

| Command | Description |
|----------|------------|
| `/start` | Start interaction |
| `/about` | Information about the bot |

---

## 🚀 Possible Improvements

This is intentionally minimal. You can extend it with:

- Per-user conversation memory
- Context reset command
- SQLite database storage
- Rate limiting
- Streaming responses
- Multi-model support
- Logging system
- Docker deployment
- Webhook mode instead of polling

---

## ⚠️ Important Notes

- Gemini Flash has a limited context window.
- This bot does not store conversation history by default.
- Designed for private usage (whitelisted users).
- Not production-scaled.

---

## 🎯 Purpose of This Project

This bot is not meant to compete with enterprise AI solutions.  
It is a learning project — a clean and simple example of how to:

- Work with Telegram API
- Connect LLM models
- Structure async Python bots
- Build your own AI-powered tools

---

## 🛡 License

MIT License – feel free to use, modify, and build on top of it.

---

## 👨‍💻 Author

Developed by t.me/xmatyden  
Built as a personal learning project to explore Telegram bots and AI integrations.

---

## ❤️ Special Thanks

- **[Telegram](https://telegram.org/)**  
  For providing an open and powerful Bot API that makes it incredibly easy to build and deploy bots for millions of users worldwide.

- **[Aiogram](https://github.com/aiogram/aiogram)**  
  For an elegant, fully asynchronous framework that makes Telegram bot development clean, modern, and enjoyable.

- **[Google AI Studio](https://aistudio.google.com/)**  
  For offering accessible access to the Gemini models and making AI integration simple and developer-friendly.

- **[Gemini](https://deepmind.google/technologies/gemini/)**  
  For providing fast and efficient large language models that power the intelligence behind this bot.

- **Python Community**  
  For maintaining a powerful, beginner-friendly ecosystem that allows rapid development and experimentation.

---

If you found this useful, consider giving the repository a ⭐  
Happy coding!
