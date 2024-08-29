# age = input("Ile masz lat? ") # get input from user
# age = int(age) # convert string to integer
# if age >= 18 and age < 65:
#     print("Jesteś w wieku produkcyjnym.")
# elif age < 0:
#     print("Nie urodziłeś się jeszcze.")
# elif age < 18:
#     print("Nie jesteś pełnoletni.")
# elif age >= 65:
#     print("Jesteś emerytem.")
# else:
#     print("Niepoprawny wiek.")

light = input("what color is the light? (red, yellow, green) ")
if light == 'red':
    print("Stop")
elif light == 'yellow':
    print("Prepare to go")
elif light == 'green':
    print("Go")
else:
    print("Invalid color")