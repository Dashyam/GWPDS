# a .py file is a python program we call it as python script
# we can also call it as python module

# Single Valued Container
# Create operation - RAM
instagram_username = "Dashyam"

# Read operation
print(instagram_username, id(instagram_username))
print(instagram_username, hex(id(instagram_username)))
print(instagram_username, oct(id(instagram_username)))
print(instagram_username, bin(id(instagram_username)))

print(type(instagram_username))

username = 'Dashyam Madhok'
print(username, id(username), type(username))

# username is reference variable which will be created in stack
# value dashyam is created in a storage container of type string in heap

user = "Dashyam Madhok"
print(user, id(user), type(user))

# Reference COPY Operation

another_user = user
print(another_user, id(another_user), type(another_user))

# UPDATE Operation
user = "anaya"
print(user, id(user), type(user))

# DELETE Operation
del user
print(user, id(user), type(user))
del another_user
print(another_user, id(another_user), type(another_user))

# Dangling Pointers and memory leak

