def deco_check(func):
    def wrapper(*args):
        first = args[0]
        second = args[1]
        if first == second:
            return func(first, second, "+")
        elif first < 0 or second < 0:
            return func(first, second, "*")
        elif first > second:
            return func(first, second, "-")
        elif first < second:
            return func(first, second, "/")

    return wrapper


@deco_check
def numbers(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "*":
        return first * second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second


print(numbers(-1, 5))
print(numbers(5, 5))
print(numbers(6, 5))
print(numbers(4, 5))
