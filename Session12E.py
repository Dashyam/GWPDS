name = "john"
age = 30
email = "john@example.com"

contact = {
    "name": "john",
    "age": 30,
    "email": "john@example.com"
}


print(name, age, email)

print("name :", name, "age :", age, "email :", email)

print("name:{} age:{} email:{}".format(name, age, email))
print("name:{1} age:{2} email:{0}".format(name, age, email))
print("name:{nm} age:{ag} email:{em}".format(nm=name, ag=age, em=email))

print("name:{name} age:{age} email:{email}".format_map(contact))

