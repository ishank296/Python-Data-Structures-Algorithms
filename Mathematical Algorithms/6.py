def get_root(n):
    x = float(n)
    y = 1.0
    e = 0.000001
    while (e < x-y):
        x= (x + y)/2
        y = n/x
    return x


print get_root(64)
