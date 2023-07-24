# Explore Set

john_followers = {"fionna", "sia", "jack", "joe", "george"}
print(john_followers, type(john_followers))

numbers = list(range(10, 101, 10))
print(numbers, type(numbers))

numbers = set(numbers)
print("numbers now are :", numbers)
print("type of numbers is :", type(numbers))

numbers.add(10)
numbers.add(110)
numbers.add(20)
numbers.add(30)

print("Numbers after add are :", numbers)

numbers.pop()
numbers.pop()
print("Numbers after pop are :", numbers)

numbers.remove(50)
numbers.discard(30)
numbers.discard(60)
print("Numbers after remove are :", numbers)


john_followers = {"fionna", "sia", "jack", "joe", "george"}
jake_followers = {"anna", "kim", "lee", "joe", "harry", "mike"}
fionna_followers = {"sia", "joe"}

followers = jake_followers.intersection(fionna_followers)
followers = john_followers.intersection(fionna_followers).intersection(jake_followers)
print("Mutual followers :", followers)

print("issubset :", fionna_followers.issubset(john_followers))
print("issuperset :", john_followers.issuperset(fionna_followers))

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

C = A - B
print("C is :", C)

D = A & B
print("D is :", D)

E = A ^ B
print("E is :", E)

F = A | B
print("F is :", F)

# Explore what is symmetric difference
G = A.symmetric_difference(B)
print("G is :", G)

