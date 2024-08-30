
from copy import deepcopy
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

print('-----------------')

if 7 in grades:
    print('7 is in grades')

grades_all =  [
    [2,3,4,5,6],
    [3,4,5,6,7],
    [4,5,6,7,8],
]
print(grades_all[0])
print(grades_all[0][0])

print('-----------------')
for grades in grades_all:
    print(grades,end=' ')
    for grade in grades:
        print(grade,end=' ')
    print()

print('-----------------')
grades_2 = grades_all # we have two references to the same object, so we can change the object through both references
grades_2[0][0] = 1 # we change the object grades_all, not grades_2
print(grades_all)
grades_2 = deepcopy(grades_all) # we have two different objects