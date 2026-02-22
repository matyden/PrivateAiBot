import asyncio
import logging
from aiogram.client.default import DefaultBotProperties
from google import genai
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from config_reader import config

# AI related settings and variables
client = genai.Client(api_key=config.ai_token.get_secret_value())
AI_model = "gemini-3-flash-preview"
user_contexts = {}
MAX_HISTORY = 30

# Bot related settings and variables
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
dp = Dispatcher()
ALLOWED_USERS = config.allowed_users

def is_allowed_user(message: types.Message) -> bool:
    return message.from_user.id in ALLOWED_USERS

@dp.message(Command("start"))
async def start(message: types.Message):
    if not is_allowed_user(message):
        return await message.answer("⛔ Access denied")
    await message.answer("Let's get started! ^_^\n"
                         "Чтобы задать вопрос ИИ-ассистенту - просто отправь сообщение!📝", parse_mode=None)

@dp.message(Command("about"))
async def about(message: types.Message):
    if not is_allowed_user(message):
        return await message.answer("⛔ Access denied")
    await message.answer("👋 Привет!\n"
                         "Это частный, простой AI-бот в Telegram 🤖\n"
                         "На базе используется модель Gemini 3 Flash (имеет ограниченный контекст).\n"
                         "Поскольку это частный бот с ограниченной моделью - это, скорее, не полноценный функциональный продукт, а мой способ научится создавать полноценные боты: использовать Telegram API, подключать AI-агентов и т.п.\n"
                         "Разработчик всея Бота - @xMatyDen\n"
                         "Бот готов к работе, просто отправь сообщение!", parse_mode=None)


@dp.message(Command("reset"))
async def reset_context(message: types.Message):
    user_id = message.from_user.id
    user_contexts[user_id] = []
    await message.answer("🔄 Контекст очищен")


@dp.message(F.text)
async def get_message(message: types.Message):
    if not is_allowed_user(message):
        return await message.answer("⛔ Access denied")

    user_id = message.from_user.id
    content = message.text

    if user_id not in user_contexts:
        user_contexts[user_id] = []

    if len(user_contexts[user_id]) > MAX_HISTORY * 2:
        user_contexts[user_id] = user_contexts[user_id][-MAX_HISTORY*2:]
        logging.log(logging.INFO, f"Context window was cleaned for user {user_id}")

    user_contexts[user_id].append({"role": "user", "parts": [content]})


    await bot.send_chat_action(message.chat.id, "typing")

    responses = client.models.generate_content(
        model = AI_model,
        contents=str(user_contexts[user_id])
    )

    user_contexts[user_id].append({"role": "model", "parts": [responses.text]})

    logging.log(logging.INFO, f"Current user-s context window: {user_contexts[user_id]}")

    await message.answer(responses.text, parse_mode=None)

    print(user_contexts)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
