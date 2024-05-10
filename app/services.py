import os.path
import sqlite3
from datetime import datetime

import pandas as pd

import settings


class DBConnector:

    def __init__(self) -> None:
        self.conn = sqlite3.connect("exchange_rate.db")
        self.cursor = self.conn.cursor()
        self._create_or_get_table()

    def close_connection(self) -> None:
        self.conn.close()

    def _create_or_get_table(self) -> None:
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rate
            (time TEXT, rate REAL)
        """)
        self.conn.commit()

    def write_into_db(self, rate: float, current_time: str) -> None:
        self.cursor.execute(
            "INSERT INTO exchange_rate VALUES (?, ?)",
            (current_time, rate)
        )
        self.conn.commit()

    def get_data_from_db(self) -> list[tuple]:
        date = datetime.now().strftime("%Y-%m-%d")
        data = self.cursor.execute(
            "SELECT * FROM exchange_rate WHERE time LIKE ?",
            (f"{date}%",)
        )
        return data.fetchall()


class XLSXWriter:
    def __init__(self) -> None:
        self.file_name = f"exchange_rate_{datetime.now().strftime('%Y-%m-%d')}.xlsx"

    def write_data_to_excel(self, data: list[tuple]) -> None:
        df = pd.DataFrame(data, columns=["time", "rate"])
        df.to_excel(
            os.path.join(settings.EXCHANGE_FILES_DIRECTORY, self.file_name), index=False
        )
