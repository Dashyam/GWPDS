# MULTIVALUED Container

numbers = 10, 20, 30, 40, 50

# Read Operation
print(numbers, id(numbers), type(numbers))

data = [10, 10.2, "Hello", "WOW", 200]
print(data, id(data), type(data))

print(data[0], id(data[0]), type(data[0]))
print(data[1], id(data[1]), type(data[1]))
print(data[2], id(data[2]), type(data[2]))

my_data = data
print(my_data, id(my_data), type(my_data))
print(my_data[3])

# IMMUTABLE - TUPLE is immutable but LIST is mutable
my_data[3] = "awesome"
print(my_data[3])
