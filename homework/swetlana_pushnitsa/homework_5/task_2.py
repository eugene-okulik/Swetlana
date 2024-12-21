string_1 = "Operation result: 42"
string_2 = "Operation result: 514"
string_3 = "Performance result: 9"

string_1_index = string_1.index(":")
string_1_result = int(string_1[string_1_index:].strip(":")) + 10

string_2_index = string_2.index(":")
string_2_result = int(string_2[string_2_index:].strip(":")) + 10

string_3_index = string_3.index(":")
string_3_result = int(string_3[string_3_index:].strip(":")) + 10

print(string_1_result, string_2_result, string_3_result)
