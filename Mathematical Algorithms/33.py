'''
Print all possible combinations of r elements in a given array of size n
'''

def combine(sofar,rest,r):
    if len(sofar) == r:
        print sofar
    else:
        if len(rest) >= r-len(sofar):
            combine(sofar+rest[0],rest[1:],r)
            combine(sofar,rest[1:],r)

combine('','abcde',3)