my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": [10, 20, 30, 40, 50],
    "dict": {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5"},
    "set": {"one", 3, 6, "five", 10}
}

print(my_dict["tuple"][-1])

my_dict["list"].append(100)
my_dict["list"].pop(1)
print(my_dict["list"])

my_dict["dict"]["i am a tuple,",] = 6
my_dict["dict"].pop("one")
print(my_dict["dict"])

my_dict["set"].add("ten")
my_dict["set"] = list(my_dict["set"])
my_dict["set"].pop(1)
my_dict["set"] = set(my_dict["set"])
print(my_dict["set"])

print(my_dict)
