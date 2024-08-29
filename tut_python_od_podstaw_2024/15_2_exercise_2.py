number = None
while number != 0:
    number = input('Enter a number: ')
    number = int(number)
    if number > 0:
        print('Positive number')
    elif number < 0:
        print('Negative number')
    else:
        print('Zero')