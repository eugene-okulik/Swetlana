def deco(func):
    def wrapper(*args):
        result = func(*args)
        print("finished")
        return result
    return wrapper


@deco
def create_text(text):
    print(text)


@deco
def sum_of_two(x, y):
    print(x + y)


@deco
def hello_python():
    print("hello python!")


create_text("I love python")
sum_of_two(2, 5)
hello_python()
