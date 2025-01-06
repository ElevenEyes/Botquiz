import aiosqlite
import asyncio
import logging
from aiogram import Bot, Dispatcher
import aiosqlite
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from files_for_bot.utils import DB_NAME, dp
from files_for_bot.handlers import cmd_quiz, cmd_start, right_answer, wrong_answer

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Замените "YOUR_BOT_TOKEN" на токен, который вы получили от BotFather
API_TOKEN = '7757637741:AAHaVTf-6isex5-Pp3yxdP-nVKKciZSx9ZQ'

# Объект бота
bot = Bot(token=API_TOKEN)



       
async def create_table():
    # Создаем соединение с базой данных (если она не существует, она будет создана)
    async with aiosqlite.connect(DB_NAME) as db:
        # Создаем таблицу
        await db.execute('''CREATE TABLE IF NOT EXISTS quiz_state (user_id INTEGER PRIMARY KEY, question_index INTEGER)''')
        await db.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, score INTEGER)''')
        # Сохраняем изменения
        await db.commit()
        

# Запуск процесса поллинга новых апдейтов
async def main():

    # Запускаем создание таблицы базы данных
    await create_table()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())