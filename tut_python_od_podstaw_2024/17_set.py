names = ['John', 'Paul', 'George', 'Ringo']
names_set = set(names) # convert a list to a set

print(names) # ['John', 'Paul', 'George', 'Ringo'])
print(names_set) # {'George', 'Paul', 'John', 'Ringo'} but the order may be different, sets are unordered
print('John' in names) # True

names_set.add('Brian') # add an element to the set
print(names_set)
names_set.remove('Paul') # remove an element from the set
print(names_set)

for name in names_set:
    print(name)
# names_set[0] # TypeError: 'set' object is not subscriptable
names_set.update(['Brian', 'Freddie']) # add more than one element to the set, we must use a list or a tuple or a set
print(names_set)

#operations on sets
names_set_2 = {'John', 'Paul', 'George', 'Ringo'}
print(names_set | names_set_2) # union of sets
print(names_set & names_set_2) # intersection of sets
print(names_set - names_set_2) # difference of sets
print(names_set ^ names_set_2) # symmetric difference of sets
# alternative way
print(names_set.union(names_set_2))
print(names_set.intersection(names_set_2))
print(names_set.difference(names_set_2))
print(names_set.symmetric_difference(names_set_2))

print('---------------------')
names_set.add('John')
print(names_set) # {'George', 'Paul', 'John', 'Ringo', 'Brian', 'Freddie'}
names_set.add('John')
print(names_set) # {'George', 'Paul', 'John', 'Ringo', 'Brian', 'Freddie'}
names_set.add('Adam')

#empty set
empty_set = set() # because {} is an empty dictionary
print(type(empty_set)) # <class 'set'>