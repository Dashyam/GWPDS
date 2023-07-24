# Whatsapp Contact List

contacts  = [
    {
        "name": "John",
        "phone": "+91 99922 11222",
        "conversations": [
            "hi",
            "hello"
        ]
    },
    {
        "name": "Fionna",
        "phone": "+91 90000 11222",
        "conversations": [
            "hi",
            "hello"
        ]
    },
    {
        "name": "George",
        "phone": "+91 92311 22110",
        "conversations": [
            "hi",
            "hello"
        ]
    }
]

search_keyword = input("Enter keyword to search : ")
print("Search keyword", search_keyword)

for contact in contacts:
    # if contact["name"].lower().startswith(search_keyword.lower()):
    # if contact["name"].lower().__contains__(search_keyword.lower()):
    if contact["name"].lower().find(search_keyword.lower()) >= 0 \
            or contact["phone"].find(search_keyword) >= 0:
        print(contact)
        print("``````````````")