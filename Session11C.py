# For Each Loop or Enhanced for loop
# Work for list, tuple and set
data = list(range(10, 101, 10))
print(data)

# for idx in range(len(data)):
#     print(data[idx])

data = set(data)

for element in data:
    print(element)

student = {"rollno": 101, "name": "fionna", "age": 21}
items = student.items()
print(items)
print("Dictionary Data")
for item in items:
    print(item)

keys = student.keys()
for key in keys:
    print(key)

values = student.values()
for value in values:
    print(value)
print("key value pairs in dictionary")
for item in student:
    print(item, student[item])