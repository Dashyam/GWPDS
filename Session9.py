def compute_taxes(amount, tax):
    amount_to_pay = amount + (amount*tax/100)
    return amount_to_pay

print("compute taxes is :", compute_taxes)
print("compute taxes hashcode is :", id(compute_taxes), hex(id(compute_taxes)))

# Reference Copy
fun = compute_taxes
print("fun is:", fun)

result = fun()
print("Result is:", result)

result = fun(amount=100, tax=18)
print("result is:", result)

result = fun(100, 18)

# del compute_taxes

# result = fun(amount=120, tax=19)
# print("result is:", result)
