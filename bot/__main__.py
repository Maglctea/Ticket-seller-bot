import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.utils.gpt import send_to_gpt
from bot.settings import BOT_TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Base `/start` command

    :param message:
    :return: None
    """
    await message.answer(
        f"Привет, {message.from_user.full_name}! Я бот-продавец билетов. Введи любое сообщение, чтобы начать общение")


@dp.message()
async def message_trigger(message: types.Message) -> None:
    """
    Checks all messages and send them to gpt. Sends a chat response to the user

    :param message:
    :return: None
    """
    try:
        await message.answer('Запрос принят. Пожалуйста, ожидайте')
        response = await send_to_gpt(message.text)
        await message.answer(response)
    except:
        await message.answer('К сожалению, произошла ошибка. Попробуйте ввести запрос еще раз')


async def main() -> None:
    """
    Run bot

    :return: None
    """
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='w')
    asyncio.run(main())
