string_1 = "Operation result: 42"
string_2 = "Operation result: 54"
string_3 = "Performance result: 209"
string_4 = "Result: 2"

def add_10(string):
    string_index = string.index(":")
    result = int(string[string_index:].strip(":")) + 10
    return result

strings = [string_1, string_2, string_3, string_4]

for s in strings:
    print(add_10(s))
