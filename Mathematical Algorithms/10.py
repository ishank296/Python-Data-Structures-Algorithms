def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def fib1(n):
    arr=[0 for i in range(n+1)]
    arr[0]=0
    arr[1]=1
    for i in range(2,n+1):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[n]

        
        
print fib(10)