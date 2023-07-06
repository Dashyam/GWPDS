# CASE STUDY
# Zomato with python storage containers


promo_codes = ["WELCOME50", "ZOMPAYTM", "BINGO", "JUMBO"]

dish1 = {
    "name": "Aloo tikki",
    "price": 100,
    "ratings": 3.7

}

dish2 = {
    "name": "Mcpuff",
    "price": 150,
    "ratings": 3.9
}

dish3 = {
    "name": "Mcveggie wrap",
    "price": 240,
    "ratings": 4.7

}
menu = [dish1, dish2, dish3, {"name": "McEgg", "price": 300, "ratings": 5.1}]
restaurant = {
    "name": "McDonalds",
    "Address": "Ansal Plaza, Ludhiana",
    "description": "Burger , fast food",
    "ratings": 4.5,
    "menu": menu,
    "promo_codes": promo_codes
}

print(restaurant)
