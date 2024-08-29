#loop for
for i in range(1, 5): # 1, 2, 3, 4 loop is a block of code that is executed multiple times. from 1 to 5 (not included)
    print(i)

print('---------------------')
for number in range(5): # 0, 1, 2, 3, 4 loop is a block of code that is executed multiple times. from 0 to 5 (not included)
    print(number)
# number is the name of the variable that stores the current value from the range, we can use any name
print('---------------------')
for _ in range(5): # _ means that we do not use the variable in the loop
    print('Hello')

print('---------------------')
for letter in 'Python': # P, y, t, h, o, n loop is a block of code that is executed multiple times
    print(letter)
