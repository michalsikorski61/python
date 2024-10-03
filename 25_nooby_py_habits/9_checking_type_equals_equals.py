from collections import namedtuple


def checking_type_equality():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)

    if type(p) == tuple:
        print("It's a tuple")
    else:
        print("It's not a tuple")

# most of the time this is not what you want the reason is inheritance
# a named tuple is a tuple so Point class is a tuple but it's not but it's not literally a built-in tuple, it's a subclass
# liskov substitution principle - checking type for equality is a violation of this principle
# in most cases you should use isinstance() instead

def checking_type_equality():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)

    if isinstance(p, tuple): # liskov substitution principle
        print("It's a tuple")
    else:
        print("It's not a tuple")