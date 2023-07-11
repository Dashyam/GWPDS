# Break and Continue

# floor_number = int(input("Enter the floor number: "))
#
# for floor in range(1, 11):
#     print("Elevator arrived on floor :", floor)
#
#     if floor == floor_number:
#         break

for idx in range(1, 11):
    # if idx >= 5:
    #     print("idx is:", idx)
    if idx <= 4:
        continue
    print("idx is :", idx)
