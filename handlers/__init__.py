from aiogram import Router
from handlers.comands_handler import router as comands_router

router = Router()

router.include_router(comands_router)