a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

for i in range(3):
    if b > a:
        a, b = b, a
    if c > b:
        b, c = c, b

print(f'The numbers in descending order are: {a}, {b}, {c}')