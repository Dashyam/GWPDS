"""
Session 2
Hashtable
h(x) = x%capacity

VCS with GitHub
multivalued container
Input Output
operators
"""
# MULTI VALUE CONTAINER
# TUPLE - tuples are indexed and immutable
names = "john", "jennie", "jim", "jack", "joe"

print(names)
print(names[2])
# names[2] = "Fionna" #error
# del names[1] #error
print(id(names))
print(names[0], id(names[0]))

instagram_username = "john"
print(instagram_username)
print(id(instagram_username))

print(instagram_username == names[0])
