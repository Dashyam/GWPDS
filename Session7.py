# Relationship Mapping
# 1 Restaurant has 1 menu
# 1 menu has many dishes

class Dish:

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def show(self):
        print("---------------------")
        print(f"NAME : {self.name} | \u20b9{self.price}")
        print(f"RATINGS | {self.rating}")
        print("---------------------")


class Menu:

    def __init__(self, title, num_of_dishes, dishes):
        self.title = title
        self.num_of_dishes = num_of_dishes
        self.dishes = dishes

    def show(self):
        print("^^^^^^^^^^^^^^^^^^^^^")
        print(self.title, "|", self.num_of_dishes)
        print("^^^^^^^^^^^^^^^^^^^^^")

        for idx in range(len(self.dishes)):
            self.dishes[idx].show()


class Restaurant:

    def __init__(self, name, address, phone, ratings, menu):
        self.name = name
        self.address = address
        self.phone = phone
        self.ratings = ratings
        self.menu = menu

    def show(self):
        print("===================")
        print(self.name, "|", self.ratings)
        print(self.address, "|", self.phone)
        print("===================")

        self.menu.show()


def main():
    dish1 = Dish(name="Dal Makhani", price=670, rating=4.8)
    dish2 = Dish(name="Paneer Do Pyaza", price=700, rating=5.0)
    dish3 = Dish(name="Kadhai Paneer", price=690, rating=4.5)

    dishes = [Dish(name="Dum Aloo", price=580, rating=4.7), dish1, dish2, dish3]

    menu = Menu(title="Indian", num_of_dishes=len(dishes), dishes=dishes)

    restaurant1 = Restaurant(name="Maharaja Plazzo",
                             address="Dugri Phase I",
                             phone="+91 99988 99988",
                             ratings=4.5,
                             menu=menu)

    restaurant1.show()

if __name__ == "__main__":
    main()
