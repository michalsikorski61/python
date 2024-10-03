def never_using_comprenhensions():
    squares = []
    for i in range(10):
        squares[i] = i * i

#or they do comprehension if they do use comprehensions only list comprehensions
# a lot of code can be maed shorter and cleaner with comprehensions

def never_using_comprehensions():
    squares = {i: i * i for i in range(10)}

# you can add dict, list, set and even generator comprehensions
def never_using_comprehensions():
    dict_comp = {i: i * i for i in range(10)}
    list_comp = [x*x for x in range(10)]
    set_comp = {i%3 for i in range(10)}
    gen_comp = (2*x+5 for x in range(10))
