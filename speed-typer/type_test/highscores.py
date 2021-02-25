import os
import pickle
import datetime
from typing import List


# CONSTANTS
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_PATH, "data")
PICKLE_PATH = os.path.join(DATA_PATH, "highscores.pkl")
BACKUP_PATH = os.path.join(DATA_PATH, "backup_highscores.pkl")


class Highscores:
    def __init__(self):
        self.today = datetime.datetime.today()
        self.date = str(self.today.date())

        self.load_data()

    def exists_pickle(self):
        """Returns True if main pickle file exists."""

        return os.path.exists(PICKLE_PATH)

    def exists_backup(self):
        """Returns True if backup pickle file exists."""

        return os.path.exists(BACKUP_PATH)

    def load_data(self):
        """Loads pickle data to self.data if a pickle exists, otherwise it gives
        a default value to self.data."""

        if self.exists_pickle():
            path = PICKLE_PATH
        elif self.exists_backup():
            path = BACKUP_PATH
        else:
            self.data = {
                "daily-highscores": [f"{self.date}: 0"],
                "all-time-highscore": f"{self.date}: 0",
            }
            return None

        with open(path, "rb") as data_pickle:
            self.data = pickle.load(data_pickle)
            # Add highscore line for current day if one does not exist
            if self.data["daily-highscores"][-1][:10] != str(self.date):
                self.data["daily-highscores"].append(f"{self.date}: 0")

    def set_stats(self):
        """Sets current wpm stats from self.data."""

        self.today_wpm = int(self.data["daily-highscores"][-1].split()[-1])
        self.all_time_wpm = int(self.data["all-time-highscore"].split()[-1])

    def get_wpm(self):
        """Returns the daily and all time highest wpm.

        Used to display wpm scores on main menu.
        """

        self.set_stats()

        return self.today_wpm, self.all_time_wpm

    def delete_backup(self):
        """Deletes the backup pickle file, if it exists."""

        if self.exists_backup():
            os.remove(BACKUP_PATH)

    def make_backup(self):
        """Turns current pickle file into a backup file, and deletes old backup."""

        self.delete_backup()

        os.rename(PICKLE_PATH, BACKUP_PATH)

    def save_data(self):
        """Saves data to a pickle file."""

        if self.exists_pickle():
            self.make_backup()

        with open(PICKLE_PATH, "wb") as data_pickle:
            pickle.dump(self.data, data_pickle)

    def check_all_time_highscore(self, score: int) -> bool:
        """Returns True if highscore provided is greater than the all time highscore."""

        self.set_stats()

        return score > self.all_time_wpm

    def check_daily_highscore(self, score: int) -> bool:
        """Returns True if highscore provided is greater than today's highscore."""

        self.set_stats()

        return score > self.today_wpm

    def add_daily_highscore(self, score: int) -> None:
        """Adds a highscore to self.data for today."""

        # Remove old daily highscore
        self.data["daily-highscores"].pop()

        self.data["daily-highscores"].append(f"{self.date}: {score}")

    def add_all_time_highscore(self, score: int) -> None:
        """Adds a daily and all time highscore to self.data."""
        self.add_daily_highscore(score)

        self.data["all-time-highscore"] = f"{self.date}: {score}"

    def delete_daily_highscore(self):
        """Deletes current daily highscore."""

        self.add_daily_highscore(0)
        self.save_data()

    def delete_all_time_highscore(self):
        """Deletes the current all-time highscore, and also today's highscore."""

        self.add_all_time_highscore(0)
        self.save_data()

    def delete_all_highscores(self):
        """Deletes all daily highscore and all-time highscore data."""

        self.data["daily-highscores"] = [f"{self.date}: 0"]
        self.delete_all_time_highscore()

    def get_datetime_object(self, date: str) -> datetime.datetime:
        """
        Returns a datetime object from a given string.
        The string must be in the format yyyy-mm-dd.
        """

        # Convert string into a list of integers
        numerical_date: list = list(map(int, date.split("-")))

        return datetime.datetime(
            numerical_date[0], numerical_date[1], numerical_date[2]
        )

    def days_since_set(self) -> int:
        """Returns the number of days since the all-time highscore was set."""

        # Get the date section from the all-time highscore
        # then get a datetime object for that date
        string_date: str = self.data["all-time-highscore"].split(":")[0]
        date_set: datetime.datetime = self.get_datetime_object(string_date)

        # Get a timedelta object representing the time between today and date_set
        difference: datetime.timedelta = self.today - date_set

        return difference.days

    # Main
    def update(self, score: int) -> str:
        """Main function, checks if a given score is a highscore then saves that
        value to self.data and to a pickle file.

        Returns string representing whether value was a daily or all time highscore.
        """

        if self.check_all_time_highscore(score):
            self.add_all_time_highscore(score)
            self.save_data()
            return "all-time"

        elif self.check_daily_highscore(score):
            self.add_daily_highscore(score)
            self.save_data()
            return "daily"

        else:
            return "none"

    def get_stats_dailies(self) -> List[str]:
        """
        Returns self.data["daily-highscores"] as raw data to be used
        in the plotting of a graph.
        """

        return self.data["daily-highscores"]


if __name__ == "__main__":
    highscore = Highscores()

    print(highscore.update(1))
    print(highscore.update(2))
    print(highscore.update(1))