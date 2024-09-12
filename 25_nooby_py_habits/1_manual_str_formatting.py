# def manual_str_formatting(name,subscriber):
#     if subscriber > 100000:
#         print("Wow " + name + "! You have " + str(subscriber) + " subscribers!")
#     else:
#         print("Lol " + name + " that's not many subs!")

# manual_str_formatting('Kamil', 1000000)

# instead use f strings for string formatting 
def manual_str_formatting(name,subscriber):
    if subscriber > 100000:
        print(f"Wow {name}! You have {subscriber} subscribers!")
    else:
        print(f"Lol {name} that's not many subs!")