"""
    Another brick in the wall

    john : 1 2 3
    jack : 2 4 6
    total bricks : 13
"""

total_bricks = int(input("Enter total number of bricks"))
bricks_in_wall = 0

for idx in range(1, total_bricks):
    john_bricks = idx
    bricks_in_wall += john_bricks

    if bricks_in_wall >= total_bricks:
        difference = bricks_in_wall - total_bricks
        print(difference)
        print("John placed the last brick:", (john_bricks - difference))
        break

    jack_bricks = idx*2
    bricks_in_wall += john_bricks
    if bricks_in_wall >= total_bricks:
        difference = bricks_in_wall - total_bricks
        print(difference)
        print("John placed the last brick:", (john_bricks - difference))
        break

print("Bricks in wall is", bricks_in_wall - difference)
