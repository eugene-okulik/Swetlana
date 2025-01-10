temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25,
    27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

hot_days = filter(lambda x: x > 28, temperatures)


def avr_temp(x):
    return sum(x) / len(x)


print(f"Hot days are: {list(hot_days)}")
print(f"The maximum temperature is {max(temperatures)}. The minimum temperature is {min(temperatures)}. "
      f"Average temperature is {avr_temp(temperatures):,.2f}")
