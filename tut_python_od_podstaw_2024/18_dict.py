phone_book = {
    "John": 123456789,
    "Paul": 987654321,
    "George": 456789123,
}

print(phone_book.get(0)) # None
print(phone_book.get("John")) # 123456789 
print(phone_book["George"]) # 456789123
#but what when the key does not exist?
# print(phone_book["Ringo"]) # KeyError: 'Ringo'
print(phone_book.get("Ringo",'Brak')) # None
#to add a new element you can use the assignment operator or the update method
phone_book["Ringo"] = 123123123
print(phone_book)
phone_book.update({"Brian": 321321321})
print(phone_book)

# to remove an element you can use the del statement or the pop method
del phone_book["John"]
print(phone_book)
print(phone_book.pop("Paul"))
print(phone_book)
# we can't have duplicates in the keys
phone_book["John"] = 123456789
print(phone_book)
phone_book["John"] = 987654321
print(phone_book)

for item in phone_book:
    print(item) # print the keys

for item in phone_book.values():
    print(item) # print the values

for key, value in phone_book.items():
    print(key, value) # print the keys and the values

# we can have a dictionary of dictionaries
phone_book = {
    "John": {
        "phone": 123456789,
        "email": "ddd",
    },
    "Paul": {
        "phone": 987654321,
        "email": "eee",
    },
    "George": {
        "phone": 456789123,
        "email": "fff",
    },
}