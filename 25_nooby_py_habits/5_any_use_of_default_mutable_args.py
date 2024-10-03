def append(n,l=[]):
    l.append(n)
    return l

l1 = append(0) # [0]
l2 = append(1) # [0,1] oops ,should be [1]


# args default are defined when the fn is defined, not when it's called
# so the default mutable args are shared between calls, in this case the list
# is shared between calls to append

#right way to do it
def append(n,l=None):
    if l is None:
        l = []
    l.append(n)
    return l

l1 = append(0) # [0]
l2 = append(1) # [1]