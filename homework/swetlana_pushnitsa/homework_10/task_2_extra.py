def deco(count):
    def inner(func):
        def wrapper(*args):
            for _ in range(count):
                func(*args)
        return wrapper
    return inner


@deco(count=5)
def example(text, x):
    print(text, x)


example("I love python", "text")
