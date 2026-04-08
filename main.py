from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import asyncio
import logging


async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Понимать что происходит
    bot = Bot(token=BOT_TOKEN)  # Подключение к серверам
    dp = Dispatcher()  # Получить update
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())