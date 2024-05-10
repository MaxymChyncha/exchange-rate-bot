import asyncio
import logging
import os
import sys

from aiogram import Bot, types, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import FSInputFile

import settings
from services import DBConnector, XLSXWriter

dp = Dispatcher()


@dp.message(Command("get_exchange_rate"))
async def send_exchange_rate_file(message: types.Message) -> None:
    connector = DBConnector()
    writer = XLSXWriter()
    data = connector.get_data_from_db()
    writer.write_data_to_excel(data)
    await message.answer_document(
        FSInputFile(
            os.path.join(
                settings.EXCHANGE_FILES_DIRECTORY, writer.file_name
            )
        )
    )


async def main() -> None:
    bot = Bot(
        token=settings.TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
