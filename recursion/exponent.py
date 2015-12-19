def exponent(k,n):
    if n == 0:
        return 1
    else:
        return k * exponent(k,n-1) 
