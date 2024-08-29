name = input("Jak masz na imię? ") # get input from user
age = int(input("Ile masz lat? ")) # get input from user
print(f"Cześć {name}!") # print text and variable to console, f-string
print(f"Masz {age} lat.") # print text and variable to console, f-string
if age >= 18: # if statement, condition
    print("Jesteś pełnoletni.") # print text to console
else:
    print("Nie jesteś pełnoletni.")