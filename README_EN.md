# 📖 StepByWord — Telegram Bot for Learning English Words

This bot helps you learn new English words every day.  
It automatically sends a "word of the day" in Telegram or allows you to get one instantly by pressing a button.  

---

## 🚀 Features
- 📩 Automatic **word of the day** at 10:00.  
- 🔘 Button "I want to learn a new word" for instant word delivery.  
- 📚 Built-in dictionary with 30+ English words including transcription and translation.  
- 🔄 Words repeat in a cycle — after the last one, it starts again.  
- ⚙️ Ready for deployment on **Render** (runs 24/7).  

---

## 🛠️ Installation & Run

### Locally
1. Clone repository:
   ```bash
   git clone https://github.com/<your-username>/english-bot.git
   cd english-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run:
   ```bash
   python bot.py
   ```

> ⚠️ Before running, add an environment variable `TOKEN` (your token from BotFather).

---

### On Render (recommended)
1. Upload project to GitHub.  
2. Connect the repository on [Render](https://render.com).  
3. Configure Render settings:
   - **Build Command**:
     ```
     pip install -r requirements.txt
     ```
   - **Start Command**:
     ```
     bash start.sh
     ```
   - In **Environment Variables** add:
     ```
     TOKEN=<your_bot_token>
     ```

4. Press **Deploy** — bot will run 24/7 🚀  

---

## 📚 Example Message
```
✨ Word of the Day ✨

resilience [rɪˈzɪl.jəns]
🇷🇺 устойчивость, жизнестойкость
```

---

## 📌 Technologies
- Python 3
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- schedule
- Render (deployment)

---

## 💡 Future Improvements
- Add more words (100+).  
- Create categories (business, travel, philosophy).  
- Add word pronunciation 🎧.  
- Track learned words.  
