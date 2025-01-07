words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def how_many_times():
    new_coll = []
    for word, number in words.items():
        repeated_num = word * number
        new_coll.append(repeated_num)
    return "\n".join(new_coll)

print(how_many_times())
