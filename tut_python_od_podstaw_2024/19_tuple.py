names = 'Kamil', 'Adam', 'John', 'Paul', 'George', 'Ringo' # tuple
print(names)
names = ('Kamil', 'Adam', 'John', 'Paul', 'George', 'Ringo') # also tuple
print(names)
print(names[0]) # Kamil 
print(names[-1]) # Ringo negative numbers are allowed it's like counting from the end
print(names[1:3]) # ('Adam', 'John') the second index is exclusive
print(names[1:]) # ('Adam', 'John', 'Paul', 'George', 'Ringo') the second index is the end
print(names[:3]) # ('Kamil', 'Adam', 'John') the first index is the beginning
print(names[::2]) # ('Kamil', 'John', 'George') step 2
print(names[::-1]) # ('Ringo', 'George', 'Paul', 'John', 'Adam', 'Kamil') reverse
print('Kamil' in names) # True
#try deleting an element or changing the value of an element
# del names[0] # TypeError: 'tuple' object doesn't support item deletion
# names[0] = 'Brian' # TypeError: 'tuple' object does not support item assignment
# names.append('Brian') # AttributeError: 'tuple' object has no attribute 'append'
# names.insert(2, 'Freddie') # AttributeError: 'tuple' object has no attribute 'insert'
# names.remove('Paul') # AttributeError: 'tuple' object has no attribute 'remove'
# names.pop() # AttributeError: 'tuple' object has no attribute 'pop'
# names.reverse() # AttributeError: 'tuple' object has no attribute 'reverse'
# names.sort() # AttributeError: 'tuple' object has no attribute 'sort'
# names.extend(['Brian', 'Freddie']) # AttributeError: 'tuple' object has no attribute 'extend'
# names.sort(reverse=True) # AttributeError: 'tuple' object has no attribute 'sort'
# we can't modify a tuple, but we can create a new one
names = names + ('Brian', 'Freddie')
print(names)
# we can have a tuple of tuples
names = (
    ('Kamil', 'Miller'),
    ('Adam', 'Smith'),
    ('John', 'Brown'),
    ('Paul', 'White'),
    ('George', 'Black'),
    ('Ringo', 'Green'),
)
print(names)
# we can have a tuple of lists
names = (
    ['Kamil', 'Miller'],
    ['Adam', 'Smith'],
    ['John', 'Brown'],
    ['Paul', 'White'],
    ['George', 'Black'],
    ['Ringo', 'Green'],
)
# tuple usually is used when we want to have a collection of elements that we don't want to change
# tuple is faster than a list
# tuple is hashable, list is not
# tuple can be a key in a dictionary, list can't
# tuple can be an element of a set, list can't
# tuple is an immutable object, list is mutable
# tuple is a sequence, list is a sequence
# tuple is a collection of elements, list is a collection of elements
# tuple is a fixed size, list is a variable size
# tuple is a heterogeneous collection, list is a heterogeneous collection
# tuple can have a mix of types, list can have a mix of types
# tuple is a sequence of elements, list is a sequence of elements
# tuple is a collection of elements, list is a collection of elements
