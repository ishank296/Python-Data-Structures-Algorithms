def exponent(k,n):
    if n == 0:
        return 1
    else:
        return k * exponent(k,n-1) 

        
def recursion2(k,n):
    if n==0:
        return 1
    else:
        ans = recursion2(k,n/2)
        if n%2 == 0:
            return ans * ans
        else:
            return ans * ans * k
