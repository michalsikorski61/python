def fn_test():
    return"function"

def add(x):
    print(x + 1)

add(2)

def add(x,y=1):
    return x + y

result = add(2,10)
print(result)