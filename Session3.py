"""
Session3
CONTROLLER
  Operators             -> Mathematical computations
  Conditional instructs -> Decision-Making
  Loops/Iterations      -> Repetition

"""
# Operators
# Arithmatic Operators
# +, -, /, *, **, //, %

product_price = 125.25
taxes = 0.18
# Associativity and Precedence of operators
price_to_pay = product_price + (product_price * taxes)
print(f"Price to pay: \u20b9 {price_to_pay}")

number = 10
result = number / 3  # Floating point division
result2 = number // 3  # Integral division
print("Result: ", result)
print("Result2: ", result2)

base = 2
result = base * 3
print("Result: ", result)

result = base ** result
print("Result: ", result)

# Assignment Operators
# =, +=, -=, *=, **=, /=, //=, %=

age = 20
# age = age + 3
age += 3  # Shorthand operation
age += 10
age -= 5
age %= 3
print("Age is:", age)

# Increment and decrement operators
# ++ and -- operators does not exist in python

idx = 0
idx += 2
idx -= 1
print("idx is :",  idx)

