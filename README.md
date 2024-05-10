# Exchange Rate Bot

## Features
- Web Scraping: Use Requests & BeautifulSoup to extract information about exchange rates and write it in DB.
- Telegram Bot: Provides command that uploads XLSX file with current daily exchange rate statistics.

## Installation

To clone this project from GitHub, follow these steps:

1. **Open your terminal or command prompt.**
2. **Navigate to the directory where you want to clone the project.**
3. **Run the following commands:**
```shell
git clone https://github.com/MaxymChyncha/exchange-rate-bot.git
python -m venv venv
source venv/bin/activate  #for Windows use: venv\Scripts\activate
```

4. **Install requirements:**

```shell
pip install -r requirements.txt
```

5. **Run the Web Scraping Script:**
```shell
python app/parser.py
```

6. **Run the Telegram Bot:**
```shell
python app/bot.py
```

7. **Work with Telegram Bot:**

Firstly, you need to get a link for your Bot that you can take while creating your bot and share it.

To create your bot, follow this link - https://t.me/BotFather

For now, a bot has only one command:
```/get_exchange_rate``` with which you can get XLSX file with daily exchange rate statistics.

## Files Structure

- `app/`: Directory with project
- `files/`: Directory for saving files with exchange rate statistics
- `bot.py`: Module that contains application for running Telegram Bot
- `parser.py`: Module that contains application for running Parser
- `services.py`: Module that contains services for work with DB and file writer
- `settings.py`: Module that contains settings for application
