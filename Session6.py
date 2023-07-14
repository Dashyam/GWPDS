"""
    OOPS
    1. Think of an object
    Restaurant : name, phone, emails, operating hours, ratings, category

"""

# 2. Create it's class
class Restaurant:
    pass

# 3. From the class create real objects in memory :)
# Object Construction statement
restaurant1 = Restaurant()
restaurant2 = Restaurant()
restaurant3 = restaurant1  # Reference Copy

# LHS restaurant1: is reference variable
# RHS Restaurant() -> Creating an object in HEAP in memory/RAM

print("Restaurant1 is ", restaurant1, id(restaurant1), hex(id(restaurant1)), type(restaurant1))
print("Data inside Restaurant1 is :", vars(restaurant1))

print("Restaurant1 is:", restaurant1)
print("Restaurant2 is:", restaurant2)
print("Restaurant3 is:", restaurant3)

# Operations on Object
# 1. Write operation
restaurant1.name = "Table by Basant"
restaurant1.phone = "+91 98989 11221"
restaurant1.email = "table@basant.com"
restaurant1.operating_hours = "11:00 to 22:00 hrs"
restaurant1.ratings = 4.7
restaurant1.category = "indian, chinese, pure veg"

restaurant2.name = "McDonalds"
restaurant2.phone = "+91 88889 99998"
restaurant2.email = "mc@donalds.com"

print("Data inside Restaurant1 now is:", vars(restaurant1))
print("Data inside Restaurant2 now is:", vars(restaurant2))
print("Data inside Restaurant3 now is:", vars(restaurant3))

# 2. Update Operation
restaurant2.phone_number = "+91 99229 11922"
restaurant3.name = "TABLE BY BASANT"
restaurant3.email = "table@table,org"
print()
print("Data inside Restaurant1 now is:", vars(restaurant1))
print("Data inside Restaurant2 now is:", vars(restaurant2))
print("Data inside Restaurant3 now is:", vars(restaurant3))

# 3. Delete Operation
del restaurant1.category
del restaurant2.email
print()
print("Data inside Restaurant1 now is:", vars(restaurant1))
print("Data inside Restaurant2 now is:", vars(restaurant2))
print("Data inside Restaurant3 now is:", vars(restaurant3))

# 4. Read Operation
print()
print(restaurant1.name)
print(restaurant2.name)
print(restaurant3.name)

# 5. Delete Operation
del restaurant1
print()
print("Data inside Restaurant1 now is:", vars(restaurant1))
