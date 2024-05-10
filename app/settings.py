import os
from dotenv import load_dotenv

load_dotenv()

# URL for scraping information about current exchange rate
EXCHANGE_RATE_URL = "https://www.google.com/finance/quote/USD-UAH"

# Path to folder for saving files with daily exchange rate statistic
EXCHANGE_FILES_DIRECTORY = os.path.join("app", "files")

# Key for Telegram bot
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
