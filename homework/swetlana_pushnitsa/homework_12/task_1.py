from enum import Enum


class FormFlower(Enum):
    tlp = "tulip"
    rs = "rose"
    gr = "green"


class TypeTulip(Enum):
    Ft = "Foster"
    Gs = "Gesner"
    Km = "Kaufmann"


class Flower:
    flower_shop = "Hortensia"

    def __init__(self, name, color, fresh, price, flower_form: FormFlower):
        self.name = name
        self.__color = color
        self.__fresh = fresh
        self.__price = price
        self.form = flower_form

    def form_flower(self):
        match self.form:
            case FormFlower.tlp:
                return "round"
            case FormFlower.rs:
                return "geometric"
            case FormFlower.gr:
                return "long leaf"

    def color(self):
        return self.__color

    def fresh(self):
        return self.__fresh

    def price(self):
        return self.__price


class Rose(Flower):

    def __init__(self, name, color, fresh, price, flower_form: FormFlower, thorns):
        super().__init__(name, color, fresh, price, flower_form)
        self.thorns = thorns


class Tulip(Flower):

    def __init__(self, name, color, fresh, price, flower_form: FormFlower, type_tulip: TypeTulip):
        super().__init__(name, color, fresh, price, flower_form)
        self.type_t = type_tulip

    def type_tulip(self):
        match self.type_t:
            case TypeTulip.Ft:
                return "Foster"
            case TypeTulip.Gs:
                return "Gesner"
            case TypeTulip.Km:
                return "Kaufmann"


class Green(Flower):

    def __init__(self, name, color, fresh, price, flower_form: FormFlower):
        super().__init__(name, color, fresh, price, flower_form)


flower1 = Rose("Tea Rose", "red", 1, 47, FormFlower.rs, "Thorns there are")
flower2 = Rose("Classic Rose", "white", 3, 37, FormFlower.rs, "There isn't thorns")
flower3 = Tulip("Tulip small", "yellow", 1, 34, FormFlower.tlp, TypeTulip.Gs)
flower4 = Tulip("Tulip big", "blue", 3, 60, FormFlower.tlp, TypeTulip.Ft)
flower5 = Green("Deco Greens", "green", 3, 12, FormFlower.gr)
flower6 = Green("Deco Whites", "white", 2, 10, FormFlower.gr)


class Bouquet:
    __flowers = None

    def __init__(self, flowers):
        self.__flowers = flowers

    def bouquet_withering(self):
        sorted_result = [x.fresh() for x in self.__flowers]
        result = sum(sorted_result) / len(sorted_result)
        return result

    def sorting_fresh(self):
        sorted_result = sorted(self.__flowers, key=lambda item: item.fresh())
        return sorted_result

    def sorting_price(self):
        sorted_result = sorted(self.__flowers, key=lambda x: x.price())
        return sorted_result

    def search_flower_by_color(self, color):
        for flower in self.__flowers:
            if color == flower.color():
                return flower
        return None

    def price_bouquet(self):
        sorted_result = [x.price() for x in self.__flowers]
        result = sum(sorted_result)
        return result


bouquet1 = Bouquet([flower2, flower3, flower6, flower4])
bouquet2 = Bouquet([flower1, flower5])
bouquet3 = Bouquet([flower5, flower1, flower4])
bouquet4 = Bouquet([flower3, flower4, flower6])


def search_color(color):
    flower = bouquet1.search_flower_by_color(color)
    if flower is not None:
        return f"This flower {flower.name} has a {color} color"
    else:
        return "There isn't flower with this color here"


def avg_fresh(obj):
    return f"The average fresh time for this bouquet is {obj.bouquet_withering()}"


def flower_sorted_by_price(obj):
    for flower in obj.sorting_price():
        return f"The cheapest flower in this bouquet is {flower.name} with price {flower.price()}$"


def flower_sorted_by_fresh(obj):
    for flower in obj.sorting_fresh():
        if flower.fresh() == 1:
            return f"The fresher flower in this bouquet is {flower.name} with fresh time {flower.fresh()} day"
        else:
            return f"The fresher flower in this bouquet is {flower.name} with fresh time {flower.fresh()} days"


def price_bouquet(obj):
    return f"The full price for this bouquet is {obj.price_bouquet()}$"


print(search_color("yellow"))
print(avg_fresh(bouquet2))
print(flower_sorted_by_fresh(bouquet3))
print(flower_sorted_by_price(bouquet4))
print(price_bouquet(bouquet4))
