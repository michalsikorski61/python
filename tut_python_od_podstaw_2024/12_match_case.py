light = input("what color is the light? (red, yellow, green) ")
match light:
    case 'red': # case with single statement
        print("Stop")
    case 'yellow': # case with single statement
        print("Prepare to go")
    case 'green': # case with single statements
        print("Go")
    case _: # default case
        print("Invalid color")