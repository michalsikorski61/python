isSkyBlue = True
isPythonDifficult = False

print(isSkyBlue and isPythonDifficult) # False because one of the values is False
print(isSkyBlue or isPythonDifficult) # True because one of the values is True
print(not isSkyBlue) # False
print(not isPythonDifficult) # True
# print(isSkyBlue && isPythonDifficult) # SyntaxError: invalid syntax
# print(isSkyBlue || isPythonDifficult) # SyntaxError: invalid syntax
# print(!isSkyBlue) # SyntaxError: invalid syntax
# print(!isPythonDifficult) # SyntaxError: invalid syntax
# print(isSkyBlue and) # SyntaxError: invalid syntax
print('---------------------')
a = 5
b = 10
print(a < b and a > 0) # True
print(a < b and a < 0) # False
# or
print(a < b or a > 0) # True
print(a > 10 or (a < 0 and a > 5)) # False
#not 
c = 10
print(not a < b) # False
print( c % 2 == 0) # True
print(not c % 2 == 0) # False

print('---------------------')
user_logged_in = True

if user_logged_in:
    print("Witaj!")
else:
    print("Zaloguj się.")

if not user_logged_in:
    print("Zaloguj się.")