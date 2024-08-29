# random game
# 1. computer draws a number from 1 to 100
# 2. the user tries to guess the number
# 3. if the user guesses the number, the game ends
# 4. if the user does not guess the number, the computer gives a hint: "more" or "less"
# 5. the user tries to guess the number again
# 6. the game continues until the user guesses the number

import random

comp_number = random.randint(1, 100)
# print('Computer number:', comp_number)

while True:
    user_number = int(input('Guess the number (1-100): '))
    if user_number == comp_number:
        print('You guessed the number')
        break
    elif user_number > comp_number:
        print('Too much')
    else:
        print('Too little')