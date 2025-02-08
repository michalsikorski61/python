i = 5

while i < 5:
    print(i)
    i += 1
print("End")

i = 0
while True:
    print(i)
    if i == 4:
        i+=2
        continue
    i += 1
    if i == 10:
        break
print("End 2")

print("-------------------")
i=0
while True:
    i+=1
    if i % 2 == 1:
        continue
    print(i)
    if i > 10:
        break
print("end 3")