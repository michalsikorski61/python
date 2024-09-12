# def bare_except():
#     while True:
#         try:
#             s = input("Input a number: ")
#             x = int(s)
#             break
#         except: # oops can't ctrl+c to exit
#             print('Not a number, try again')

#  instead use this
def bare_except():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except ValueError: # oops can't ctrl+c to exit
            print('Not a number, try again')