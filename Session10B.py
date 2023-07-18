"""
     Multi Value Containers
        Sequences:
            Tuple
            List
            Set
            String


        Dictionary


    Properties:
        1. Indexing
        2. Negative Indexing
        3. Slicing
        4. Concatenation
        5. Multiplicity
        6. Membership testing
"""
# 1D List
my_data = [10, 20, 30]

# 2D List
numbers = [
    [10, 20, 30],
    [40, 50, 60, 70],
    [90, 99]
]

large_data = [
    [
        [10, 20, 30],
        [40, 50, 60, 70],
        [90, 99]
    ],
    [
        [10, 20, 30],
        [40, 50, 60, 70],
        [90, 99]
    ]
]


# 1. Indexing
print(f"len(my_data) : {len(my_data)}")
print(f"my_data[1] : {my_data[1]}")

print(f"len(numbers) : {len(numbers)}")
print(f"numbers[1] : {numbers[1]}")   # Entire List
print(f"numbers[1][2] : {numbers[1][2]}")  # 60

print(f"len(large_data) : {len(large_data)}")
print(f"large_data[1][2][0] : {large_data[1][2][0]}")  # 90

# 2. Negative Indexing

print(f"my_data[-1] : {my_data[-1]}")  # 30
print(f"numbers[-2][-1] : {numbers[-2][-1] }")  # 70
print(f"large_data[-1][-3][-3] : {large_data[-1][-3][-3]}")  # 10

# 3. Slicing

data = list(range(10, 101, 10))
print("Data:", data)  # Data: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"data[:5] : {data[:5]}")  # [10, 20, 30, 40, 50]
print(f"data[6:] : {data[6:]}")  # [70, 80, 90, 100]
print(f"data[5:9] : {data[5:9]}")  # [60, 70, 80, 90]

print(f"data[:-5] : {data[:-5]}")  # [10, 20, 30, 40, 50]
print(f"data[-5:-2] : {data[-5:-2]}")  # [60, 70, 80]

# 3. Concatenation

data1 = (10, 20, 30)
data2 = (40, 50, 60)

data3 = data1 + data2
print("data3: ", data3)

# 4. Multiplicity

data4 = data1*2
print("data4: ", data4)

# 5. Membership testing

print(10 in data4)
print(20 in data1)
print(100 not in data1)

student = dict(name="John Watson", age=30, gender="male", roll=101, address="Baker Street")
print("name" in student)
