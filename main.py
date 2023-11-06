import os
import logging
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher


# Loading data from the .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up bot and dispatcher
bot = Bot(token=os.environ.get('TOKEN'))
dp = Dispatcher()


# Define main function
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
