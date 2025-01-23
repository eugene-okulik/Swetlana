PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_list = PRICE_LIST.split("\n")
list_1 = [sub.split(" ")[0] for sub in price_list]
list_2 = [sub.split(" ")[1].rstrip("р") for sub in price_list]
list_2 = map(lambda x: int(x), list_2)
dict_price_list = dict(zip(list_1, list_2))

print(dict_price_list)
