names = ['John', 'Paul', 'George', 'Ringo'] # list. Double quotes are also allowed, and will be printed as single quotes

print(names)

names.append('Brian') # add an element to the end of the list
print(names[-1]) # Brian

names.insert(2, 'Freddie') # add an element at index 2
print(names)

names.remove('Paul') # remove an element
print(names)

print(names.pop()) # remove the last element and return it

print('---------------------')
for name in names:
    print(name)

del names[0] # remove an element at index 0
print(names)
del names # delete the entire list

#list comprehension
numbers = [1, 2, 3, 4, 5] # list of numbers from 1 to 5 inclusive 
squared_numbers = [number ** 2 for number in numbers] # create a new list with the squares of the numbers from the numbers list

names = ['John', 'Paul', 'George', 'Ringo']
names.remove('Paul') # remove an element of the value 'Paul'
print(names)
#  we can have duplicates
names.append('John')
print(names)
names.remove('John') # remove the first occurrence of the element of the value 'John'
print(names)
# count the number of occurrences of an element
print(names.count('John')) # 1
names.append('John')
print(names.count('John')) # 2
# find the index of the element
print(names.index('John')) # 0
print(names.index('John', 1)) # 3
# reverse the list
names.reverse()
print(names)
# sort the list
names.sort()
print(names)
names.sort(reverse=True)
print(names)
# add more than one element
names.extend(['Brian', 'Freddie'])
print(names)
# extend mix of types
names.extend([1, 2, 3, 'adam', 'john'])
print(names)

# change value of the element
names[0] = 'Adam'
print(names)