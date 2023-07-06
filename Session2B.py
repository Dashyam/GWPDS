# MULTI VALUE CONTAINER
# SET
# Output is unordered
# it does not support indexing
# it works on hashing
john_followers = {"fionna", "jack", "harry", "sia", "kim", "jack"}
print(john_followers, type(john_followers), id(john_followers))

fionna_followers = {"leo", "nab", "ben", "kim", "harry"}
print(fionna_followers, type(fionna_followers), id(fionna_followers))

mutual_followers = john_followers.intersection(fionna_followers)
print(mutual_followers, type(mutual_followers), id(mutual_followers))

mutual_list = list(mutual_followers)
print(mutual_list, type(mutual_list), id(mutual_list))

