grades = [2, 3, 4, 5, 6]
print(grades[0])  # 2
print(grades[1])  # 3
print(grades[2])  # 4

for grade in grades:
    print(grade)

print('---')
for i in range(len(grades)):
    print(grades[i],end=' ')

print()
print('---')
for i,grade in enumerate(grades):
    print(i,grade)

print('---')
for i,grade in enumerate(grades):
    grades[i] = grade + 1

grades.append(6)
grades.extend([7,8])# we must give a list or any iterable object
grades.insert(0,1) # we must give an index and a value
print(grades)
# how to find an index of a value
grades.remove(6) # we must give a value
print(grades)
print(grades.pop()) # 8
print(grades)
grades.sort() # or sorted(grades)
print(grades) 
grades.sort(reverse=True) # or sorted(grades,reverse=True)
print(grades)
print(grades.index(5)) # 3