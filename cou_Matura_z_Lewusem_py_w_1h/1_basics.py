# for i in range(10):
#     print('Hello, World!')

for i in range(1,10): # range(1,10) returns a sequence of numbers from 1 to 9, 10 is excluded
    if i != 5:
        print(i)

for i in range(1,10,2): # range(1,10,2) returns a sequence of numbers from 1 to 9 with a step of 2
    if i == 5:
        break
    print(i)

print('-----------------')

temperture = 20
while temperture < 25:
    print('Temperture is too low')
    temperture += 1

print('-----------------')
for i in range(1,10):
    if i == 5:
        continue
    print(i)