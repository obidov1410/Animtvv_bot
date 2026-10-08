import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "BU_YERGA_TOKEN_YOZILADI"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Salom!\n\n"
        "🎌 Animtv botga xush kelibsiz!\n"
        "Anime kodini yoki nomini yuboring."
    )


async def main():
    print("Anime bot ishga tushdi!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
