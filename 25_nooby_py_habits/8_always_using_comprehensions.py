def always_using_comprehensions(a,b,c):
    """matrix product of a,b of length n x n"""
    return [
        sum(a[n * i + k] * b[n * k + j] for k in range(n))
        for i in range(n)
        for j in range(n)
    ]

# you dont need turn every single loop into a comprehension
# sometimes it actually makes the code harder to read

#instead of this
def always_using_comprehensions(a,b,c):
    """matrix product of a,b of length n x n"""
    c = []
    for i in range(n):
        for j in range(n):
            ij_entry = sum(a[n * i + k] * b[n * k + j] for k in range(n))
            c.append(ij_entry)
    return c