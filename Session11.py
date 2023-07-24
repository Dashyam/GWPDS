# Explore List in Python

numbers = list(range(10, 101, 10))
print("1. numbers :", numbers)
print("type of numbers :", type(numbers))

numbers.append(30)
numbers.append(77)
numbers.append(97)
numbers.append(30)

print("2. numbers", numbers)
print("Sum :", sum(numbers))
print("Min :", min(numbers))
print("Max :", max(numbers))
print("Length :", len(numbers))

reverse_numbers = list(reversed(numbers))
print("Reverse numbers is :", reverse_numbers)

print("Index of 50 is :", numbers.index(50))
print("Count of 30 in numbers is :", numbers.count(30))

data = [70, 30, 50, 90, 20]
print("Data is:", data)
data.sort()
print("Data in sorted arrangement is: ", data)

names = ["john", "anna", "sia", "angel", "kim"]
names.sort()
print("Names :", names)
print("Min of names :", min(names))
print("Max of names :", max(names))
# print("Sum of names :", sum(names)) # Error

names.remove("sia")
data.remove(30)

print(names)
print(data)

data = [10, 20, 30, 40, 50]
# data.pop(0)
# data.clear()
print(data)

data.insert(2, 77)
data.insert(len(data), 100)
data.insert(-1, 22)
print(data)



