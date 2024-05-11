from aiogram import Bot, Dispatcher, types
import asyncio

bot = Bot(token="1577735395:AAHYeWVDVgBiXf0in8uPGgof4pWAdNRzkMg")
dp = Dispatcher(bot=bot)

async def main():
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')
