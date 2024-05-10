import time
from datetime import datetime

import requests
import schedule
from bs4 import BeautifulSoup

import settings
from services import DBConnector


def scrape_usd_to_uah_rate() -> float:
    page = requests.get(settings.EXCHANGE_RATE_URL).content
    soup = BeautifulSoup(page, "html.parser")
    element = soup.select_one("div.fxKbKc").text.strip()
    return float(element.replace(",", "."))


def scrape_and_save_exchange_rate() -> None:
    db_connector = DBConnector()
    rate = scrape_usd_to_uah_rate()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db_connector.write_into_db(rate, current_time)
    db_connector.close_connection()

    print(f"At {current_time}, USD to UAH exchange rate is: {rate}")


if __name__ == "__main__":
    schedule.every().hour.at(":00").do(scrape_and_save_exchange_rate)
    while True:
        schedule.run_pending()
        time.sleep(1)
