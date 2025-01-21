def deco_check(func):
    def calc(*args):
        first = args[0]
        second = args[1]
        if first == second: return first + second
        elif first < 0 or second < 0: return first * second
        elif first > second: return first - second
        elif first < second: return first / second


    return calc

@deco_check
def numbers(first, second):
    print(first, second)

print(numbers(-1, 5))
print(numbers(5, 5))
print(numbers(6, 5))
print(numbers(4, 5))
