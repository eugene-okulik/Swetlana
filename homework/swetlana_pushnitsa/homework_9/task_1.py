import datetime as dt


user_datetime = "Jan 15, 2023 - 12:05:33"
python_datetime = dt.datetime.strptime(user_datetime, "%b %d, %Y - %H:%M:%S")
full_month = dt.datetime.strftime(python_datetime, "%B")
new_user_datetime = dt.datetime.strftime(python_datetime, "%d.%m.%Y, %H:%M.")

print(f"{full_month}\n{new_user_datetime}")
