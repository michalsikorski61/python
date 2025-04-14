# number = 100
# while number > 0:
#     print(number)
#     number = number // 2

# command = ""
# while command.lower() != "quit":
#     command = input(">").lower()
#     print("ECHO", command)


while True:
    command = input(">").lower()
    print("ECHO", command)
    if command.lower() == "quit":
        break
