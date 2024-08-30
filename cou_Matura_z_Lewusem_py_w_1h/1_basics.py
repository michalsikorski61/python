temp = -2
is_happy = False
if temp > 10 or is_happy:
    print(f"Go out, it's {temp} degrees")
elif temp > -10 and  not is_happy:
    print(f"Put on a jacket, it's {temp} degrees")
else:
    print(f"Stay home, it's {temp} degrees")