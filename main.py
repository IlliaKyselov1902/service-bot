import logging
import asyncio

from loader import dp, bot

# Set up logging
logging.basicConfig(level=logging.INFO)


# Define main function
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
