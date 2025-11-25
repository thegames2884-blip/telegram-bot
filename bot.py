import logging
import wikipedia
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

API_TOKEN = "8247663114:AAENLmuPK-x1o2vUHNT7NbXBHM9EpM3-ooM"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

wikipedia.set_lang("uz")

@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: Message):
    await message.answer(
        "Salom! Men Wikipedia botman.\n"
        "Menga biror mavzu yuboring, men sizga Wikipedia’dan ma’lumot topib beraman."
    )

@dp.message()
async def get_wiki(message: Message):
    query = message.text
    try:
        result = wikipedia.summary(query, sentences=3)
        await message.answer(result)
    except wikipedia.exceptions.DisambiguationError as e:
        await message.answer(f"Bu so‘z bir nechta ma’noga ega: {e.options[:5]}")
    except wikipedia.exceptions.PageError:
        await message.answer("Kechirasiz, bu mavzu bo‘yicha ma’lumot topilmadi.")
    except Exception as ex:
        await message.answer(f"Xatolik yuz berdi: {ex}")

async def main():
    # faqat pollingni ishga tushirish kifoya
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
