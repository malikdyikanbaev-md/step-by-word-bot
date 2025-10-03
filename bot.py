import telebot
from telebot import types
import schedule
import time
import threading
import traceback
import os

# 🔑 Получаем токен из переменной окружения (БЕЗ ТОКЕНА В КОДЕ!)
TOKEN = os.getenv("TOKEN")  # ← ТАК ПРАВИЛЬНО!
bot = telebot.TeleBot(TOKEN)

# 📘 Список слов (30 штук на месяц)
words = [
    {"word": "resilience", "transcription": "[rɪˈzɪl.jəns]", "translation": "устойчивость, жизнестойкость"},
    {"word": "horizon", "transcription": "[həˈraɪ.zən]", "translation": "горизонт"},
    {"word": "wander", "transcription": "[ˈwɒn.dər]", "translation": "бродить, странствовать"},
    {"word": "fleeting", "transcription": "[ˈfliː.tɪŋ]", "translation": "мимолётный"},
    {"word": "ember", "transcription": "[ˈɛm.bər]", "translation": "уголёк, тлеющий остаток"},
    {"word": "serenity", "transcription": "[səˈren.ə.ti]", "translation": "спокойствие"},
    {"word": "gratitude", "transcription": "[ˈɡræt.ɪ.tjuːd]", "translation": "благодарность"},
    {"word": "perseverance", "transcription": "[ˌpɜː.sɪˈvɪə.rəns]", "translation": "настойчивость"},
    {"word": "ephemeral", "transcription": "[ɪˈfem.ər.əl]", "translation": "недолговечный"},
    {"word": "diligence", "transcription": "[ˈdɪl.ɪ.dʒəns]", "translation": "усердие"},
    {"word": "humility", "transcription": "[hjuːˈmɪl.ɪ.ti]", "translation": "скромность, смирение"},
    {"word": "ambition", "transcription": "[æmˈbɪʃ.ən]", "translation": "стремление, амбиция"},
    {"word": "wisdom", "transcription": "[ˈwɪz.dəm]", "translation": "мудрость"},
    {"word": "freedom", "transcription": "[ˈfriː.dəm]", "translation": "свобода"},
    {"word": "hope", "transcription": "[həʊp]", "translation": "надежда"},
    {"word": "courage", "transcription": "[ˈkʌr.ɪdʒ]", "translation": "смелость"},
    {"word": "legacy", "transcription": "[ˈleɡ.ə.si]", "translation": "наследие"},
    {"word": "patience", "transcription": "[ˈpeɪ.ʃəns]", "translation": "терпение"},
    {"word": "kindness", "transcription": "[ˈkaɪnd.nəs]", "translation": "доброта"},
    {"word": "compassion", "transcription": "[kəmˈpæʃ.ən]", "translation": "сострадание"},
    {"word": "destiny", "transcription": "[ˈdes.tɪ.ni]", "translation": "судьба"},
    {"word": "strength", "transcription": "[streŋkθ]", "translation": "сила"},
    {"word": "journey", "transcription": "[ˈdʒɜː.ni]", "translation": "путешествие"},
    {"word": "purpose", "transcription": "[ˈpɜː.pəs]", "translation": "цель, предназначение"},
    {"word": "balance", "transcription": "[ˈbæl.əns]", "translation": "баланс, равновесие"},
    {"word": "growth", "transcription": "[ɡrəʊθ]", "translation": "рост, развитие"},
    {"word": "vision", "transcription": "[ˈvɪʒ.ən]", "translation": "видение"},
    {"word": "focus", "transcription": "[ˈfəʊ.kəs]", "translation": "фокус, сосредоточенность"},
    {"word": "faith", "transcription": "[feɪθ]", "translation": "вера"},
    {"word": "unity", "transcription": "[ˈjuː.nə.ti]", "translation": "единство"}
]

current_index = 0
CHAT_ID = None

# 🔔 Отправка слова
def send_word(chat_id):
    global current_index
    try:
        word = words[current_index]
        text = (
            "✨ Слово дня ✨\n\n"
            f"{word['word']} {word['transcription']}\n"
            f"🇷🇺 {word['translation']}"
        )
        bot.send_message(chat_id, text)
        print(f"[INFO] Sent '{word['word']}' to {chat_id} (index {current_index}).")
        current_index = (current_index + 1) % len(words)
    except Exception as e:
        print("[ERROR] send_word exception:", e)
        traceback.print_exc()

# 🕒 Авто-рассылка в 10:00
def scheduled_word():
    if CHAT_ID:
        send_word(CHAT_ID)
    else:
        print("[INFO] scheduled_word: CHAT_ID not set. Send /start to register chat id.")

schedule.every().day.at("10:00").do(scheduled_word)

def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Запускаем планировщик в отдельном потоке
threading.Thread(target=schedule_checker, daemon=True).start()

# 🔹 /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    print(f"[INFO] /start from {CHAT_ID}")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Хочу выучить новое слово"))

    bot.send_message(message.chat.id, 
        "Привет 👋 Я твой бот для изучения английских слов!\n"
        "Каждый день в 10:00 я пришлю тебе слово.",
        reply_markup=markup
    )

# 🔹 Кнопка
@bot.message_handler(func=lambda message: message.text and "хочу" in message.text.lower() and "слово" in message.text.lower())
def handle_button(message):
    send_word(message.chat.id)

# 🔹 /word
@bot.message_handler(commands=['word'])
def cmd_word(message):
    send_word(message.chat.id)

# 🔹 Всё остальное
@bot.message_handler(func=lambda message: True)
def handle_other(message):
    bot.reply_to(message, "Нажмите 'Хочу выучить новое слово' или подождите утреннее слово в 10:00!")
    print(f"[INFO] Unknown message from {message.chat.id}: {message.text}")

if __name__ == "__main__":
    print("🤖 Бот запущен на Railway...")
    bot.infinity_polling()