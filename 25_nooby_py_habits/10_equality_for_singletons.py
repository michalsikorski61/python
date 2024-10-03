def equality_for_singletons(x):
    if x == None:
        pass

    if x == True:
        pass

    if x == False:
        pass

# using equals x2 to check for None , True and false
# instead of equality you should check for identity using is comparison
def equality_for_singletons(x):
    if x is None:
        pass

    if x is True:
        pass

    if x is False:
        pass

# generated: 
# you can also use the fact that None, True and False are singletons
# and use the identity operator is
# this is faster and more readable
# this is also more pythonic
