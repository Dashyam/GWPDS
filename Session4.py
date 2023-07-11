# Loops
# while, for
employees = ["john", "jenny", "kim", "sia", "leo", "fionna"]
name = input("Enter Employee name to search")
print("Employee to search", name)
"""
flag = False

if name == employees[0]:
    flag = True

if name == employees[1]:
    flag = True

if name == employees[2]:
    flag = True
"""

# LINEAR SEARCH ALGO

"""
flag = False
idx = 0
while idx < 6:
    print("Matching", name, "with", employees[idx])

    if name == employees[idx]:
        flag = True
        break
    idx += 1
"""

flag = False
# for idx in range(0, 6, 1) -> 0, 1, 2, 3, 4, 5
for idx in range(6):
    print("Matching", name, "with", employees[idx])
    if name == employees[idx]:
        flag = True
        break
if flag:
    print("Name Found")
else:
    print("Name not found")
