from aiogram import Bot, Dispatcher
import asyncio
import logging
from config import BOT_TOKEN
from handlers import router


async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Понимать что происходит
    bot = Bot(token=BOT_TOKEN)  # Подключение к серверам
    dp = Dispatcher()  # Получить update
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())