from enum import Enum


class Operator(Enum):
    addition = "+"
    divide = "/"
    multiply = "*"
    subtraction = "-"


def deco_check(func):
    def wrapper(*args):
        first = args[0]
        second = args [1]
        if first == second:
            return func(first, second, Operator.addition)
        elif first < 0 or second < 0:
            return func(first, second, Operator.multiply)
        elif first > second:
            return func(first, second, Operator.subtraction)
        elif first < second:
            return func(first, second, Operator.divide)
    return wrapper


@deco_check
def numbers(first, second, operation: Operator):
    match operation:
        case operation.addition:
            return first + second
        case operation.multiply:
            return first * second
        case operation.subtraction:
            return first - second
        case operation.divide:
            return first / second


print(numbers(-1, 5))
print(numbers(5, 5))
print(numbers(6, 5))
print(numbers(4, 5))
