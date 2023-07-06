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
# List - Lists are indexed and mutable
names = ["john", "jennie", "jim", "jack", "joe"]

print(names)
print(names[2])

names[2] = "Fionna"
del names[1]

print(id(names))
print(names[0], id(names[0]))
print(names)

names.append("george")
names.append("george")
print(names)

