def add(a, b):
    print(a + b)

a = 'michal' # dynamic typing that allows to change the type of the variable, strong typing that does not allow to mix types
b = 'kowalski' # dynamic typing that allows to change the type of the variable, strong typing that does not allow to mix types
a = 2 # dynamic typing that allows to change the type of the variable, strong typing that does not allow to mix types
b = 3 # dynamic typing that allows to change the type of the variable, strong typing that does not allow to mix types
add(a, b) # 5

a = 3
b = 'michal'
# add(a, b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(a + b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print('---------------------')
a= 3
b = '3'
print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'>
print(a + int(b)) # 6

print(type(a)) # <class 'str'>
print(type(b)) # <class 'str'>

print('---------------------')
c = 'Michal'
print(type(c)) # <class 'str'>
c = 3
print(type(c)) # <class 'int'>
c = 3.0
print(type(c)) # <class 'float'>
c = True
print(type(c)) # <class 'bool'>
c = None
print(type(c)) # <class 'NoneType'>
# we can change the type of the variable in Python - redeclaration of the variable

