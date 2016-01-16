''' Pascal's Triangle '''

def factorial(n):
    if n <=1:
        return 1
    else:
        return n*factorial(n-1)

def pascal_triangle(l):
    for i in range(l):
        for j in range(i+1):
            c = factorial(i)/(factorial(j) * factorial(i-j))
            print c,
        print '\n'

pascal_triangle(6)
    