# Strings are immutable
# Strings are never modified you will get new string in memory
names = "John, Jennie, Jim, Jack, Joe"
print(f"names : {names, id(names)}")
names.upper()
print(f"names now are : {names}")
upper_case_names = names.upper()
print(f"names now are : {upper_case_names, id(upper_case_names)}")
print(f"upper_case_names check : {upper_case_names.isupper()}")
names = names + ", Kia"
print(f"names now are : {names}")

s1 = names.capitalize()
quote = 'be exceptional, have a good day'
s2 = quote.title()
s3 = names.swapcase()
s4 = names.replace("J", "L")

print(f"s1 : {s1}")
print(f"s2 : {s2}")
print(f"s3 : {s3}")
print(f"s4 : {s4}")

password = input("Enter your password : ")
# rstrip(), lstrip()
print("Password :", password.strip())

data = '0000030204212000'
print(data.strip('0'))

number = 3.210000000
number = float(str(number).strip("0"))
print(number, type(number))

message = "No Internet Connectivity"
print(message)
print(message.center(120))
print(message.ljust(120))
print(message.rjust(120))

data = "545"
print(data.zfill(50))

quote = 'search the candle rather than cursing the darkness'
print(quote.find('sing'))
print(quote.find('the'))
print(quote.index('the'))
print(quote.rindex('the'))

idx1 = quote.index('candle')
idx2 = idx1 + len('candle')

print("idx1 start :", idx1)
print("idx2 end :", idx2)

print(quote[idx1 : idx2])

for ch in quote:
    print(ch, end=" ")