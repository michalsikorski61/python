age = 29
cash = 40

if age >= 18:
    if cash >= 35:
        print('You can go to the cinema')

print('------------------')
if age >= 18 and cash >= 35:
    print('You can go to the cinema')

print('-------------------------')
if age <= 12 or cash >= 30:
    print('You can enter cinema')

print('----------------------')
if not age > 12 or cash >= 30:
    print("Can enter")
else:
    print("Can't enter")

print('---------------------------------')
if True or False and False: # and first, then or
    print("True")
else:
    print("False")

