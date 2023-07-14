from Session7 import Menu, Restaurant, Dish


def main():
    restaurant = Restaurant(name="WOK SINGH",
                            address="Rajgarh Estates",
                            phone="+91 90000 00009",
                            ratings=4.5,
                            menu=Menu(title="Chinese", num_of_dishes=5,
                                      dishes=[Dish(name="Hakka Noodles", price=350, rating=4.5),
                                              Dish(name="Dimsums", price=360, rating=4.8),
                                              Dish(name="Fried Rice", price=400, rating=5.0),
                                              Dish(name="Manchurian gravy", price=470, rating=4.6),
                                              Dish(name="Spring Roll", price=290, rating=3.7)]))
    restaurant.show()

if __name__ == "__main__":
    main()