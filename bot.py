import psycopg2
import asyncio
import logging

from os import getenv
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv
from pathlib import Path

from database import session, Members

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
#logging.getLogger('apscheduler').setLevel(logging.DEBUG)

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

bot = Bot(getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message(commands=["start"])
async def welcome_message(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='хочу участвовать',
        callback_data='continue')
    )
    await message.answer('ПРИВЕТСТВИЕ', reply_markup=builder.as_markup())

@dp.callback_query()
async def callback_query(callback: types.CallbackQuery):
    button = callback.data
    if button == 'continue':
        pass

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())