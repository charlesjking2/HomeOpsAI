from pathlib import Path
import sqlite3


class MemoryService:

    def __init__(
        self,
        database_path="data/homeops.db",
    ):
        self.database_path = database_path

        Path("data").mkdir(
            exist_ok=True
        )

        self.connection = sqlite3.connect(
            self.database_path
        )

        self.initialize()


    def initialize(self):

        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS meal_history (
                id INTEGER PRIMARY KEY,
                meal TEXT NOT NULL,
                date TEXT NOT NULL
            )
            """
        )

        self.connection.commit()


    def add_meal(
        self,
        meal,
        date,
    ):

        self.connection.execute(
            """
            INSERT INTO meal_history
            (meal, date)
            VALUES (?,?)
            """,
            (meal, date),
        )

        self.connection.commit()


    def recently_used(
        self,
        meal,
        days=14,
    ):

        result = self.connection.execute(
            """
            SELECT COUNT(*)
            FROM meal_history
            WHERE meal = ?
            """,
            (meal,),
        ).fetchone()

        return result[0] > 0