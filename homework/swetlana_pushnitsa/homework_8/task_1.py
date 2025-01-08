import random


salary = int(input("How much your salary: "))


def random_salary_bonus():
    random_bonus = bool(random.getrandbits(1))
    if random_bonus == True:
        new_salary = salary + random.randint(0, salary)
        print(f"{salary}, {random_bonus} = ${new_salary}")
    else:
        print(f"{salary}, {random_bonus} = ${salary}")


random_salary_bonus()
