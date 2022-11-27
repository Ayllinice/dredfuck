import logging
import os

from aiogram import Bot, Dispatcher, types

# log
from aiogram.utils import executor

import config

logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


# simple profanity check
@dp.message_handler()
async def echo(message: types.Message):
    if "блин" in message.text or "дура" in message.text or "Блять" in message.text or "блять" in message.text  or "блиииин" in message.text:
        print("Сообщение удалено")
        # profanity detected, remove
        await message.delete()


# run long-polling
if __name__== '__main__':
    executor.start_polling (dp, skip_updates= True)
