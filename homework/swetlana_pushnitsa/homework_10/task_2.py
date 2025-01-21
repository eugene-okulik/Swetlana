def deco(func):
    def counter(*args, **kwargs):
        for key, value in kwargs.items():
            for i in range(value):
                func(*args)
    return counter


@deco
def example(text):
    print(text)

example("I love python", count=5)
