def exponent(k,n):
    if n == 0:
        return 1
    else:
        return k * exponent(k,n-1) 

'''
divide and conquer algorithm

x^n= x^n/2 * xn/2 if n is even
x^n= x^n/2 * xn/2 * x if n is odd 
'''        
def recursion2(k,n):
    if n==0:
        return 1
    else:
        ans = recursion2(k,n/2)
        if n%2 == 0:
            return ans * ans
        else:
            return ans * ans * k

if __name__=="__main__":
    print recursion2(5,12)
