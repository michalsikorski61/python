# for number in range(1, 4):
#     print("Attempt", number, (number) * ".")


#     print("Hello World", number, (number) * ".")
successful = True
for number in range(3):
    print("Attempt")
    # if number == 2:
    #     successful = True
    if successful:
        print("Success")
        break
else:
    print("Attempted 3 times and failed")
