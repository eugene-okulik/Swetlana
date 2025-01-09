import sys


sys.set_int_max_str_digits(100001)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def place_of_number(num):
    count = 1
    for i in fibonacci_generator():
        if count == num:
            print(i)
            break
        count += 1


place_of_number(5)
place_of_number(200)
place_of_number(1000)
place_of_number(100000)
