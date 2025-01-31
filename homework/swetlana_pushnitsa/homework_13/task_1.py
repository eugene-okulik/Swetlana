import os
import datetime
import re
from datetime import timedelta


class DateTimeFileHandler:

    def __init__(self, file_name):
        base_path = os.path.dirname(__file__)
        homework_path = os.path.dirname(os.path.dirname(base_path))
        self.file_path = os.path.join(homework_path, "eugene_okulik", "hw_13", file_name)

    def __enter__(self):
        self.file = open(self.file_path, "r", encoding="utf-8")
        return self

    def __exit__(self, *args):
        self.file.close()

    def get_next_date(self):
        file_line = self.file.readline()
        date_time_format = '%Y-%m-%d %H:%M:%S.%f'
        pattern_date = r"^(\d{1}.) (\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2}.\d{6})"
        date_search = re.match(pattern_date, file_line)
        date = date_search.group(2)
        date_datetime = datetime.datetime.strptime(date, date_time_format)
        return date_datetime


with DateTimeFileHandler("data.txt") as file:
    print(file.get_next_date())
    print(file.get_next_date())
    print(file.get_next_date())














base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")
time_now = datetime.datetime.now()
date_time_format = '%Y-%m-%d %H:%M:%S.%f'
pattern_date = r"^(\d{1}.) (\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2}.\d{6})"

def read_file():
    with open(file_path, "r", encoding="utf-8")as file:
        for line in file.readlines():
            yield line
line_generator = read_file()

first_line = next(line_generator)
second_line = next(line_generator)
third_line = next(line_generator)



def formatting_of_date_time(line):
    date_search = re.match(pattern_date, line)
    date = date_search.group(2)
    date_datetime = datetime.datetime.strptime(date, date_time_format)
    return date_datetime

line_1 = formatting_of_date_time(first_line)
line_2 = formatting_of_date_time(second_line)
line_3 = formatting_of_date_time(third_line)


def in_1_week(line):
    date_in_7_days = line + timedelta(days=7)
    print(date_in_7_days)

def which_day_of_the_week(line):
    date_date = line.date()
    which_day = date_date.weekday()
    print(which_day)

def how_long_ago(line):
    how_long_date = time_now - line
    print(how_long_date)

in_1_week(line_1)
which_day_of_the_week(line_2)
how_long_ago(line_3)







