arr = [0 for i in range(10)]
choice = (1,2,3)
def print_composition(n,i):
    if n==0:
        print arr[:i]
    elif n > 0:
        for k in choice:
            arr[i]= k
            print_composition(n-k,i+1)

print_composition(5,0)
            
