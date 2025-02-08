from random import randint

# for i in range(100):
#     print(randint(1,10))
los = randint(1,10)
answer = -1
i = 0

print("I picker a num. Guess what num it is.")
while answer != los:
    i += 1
    answer = int(input("Pick: "))
    if answer < los:
        print("To little")
    elif answer > los:
        print("To much")

print(f"You win in {i} tries!")