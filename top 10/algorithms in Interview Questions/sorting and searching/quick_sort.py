def partition(a,hi,lo):
    i = lo+1
    j = lo+1
    p = a[lo]
    while (j<=hi):
        if a[j] < p:
            a[j],a[i] = a[i],a[j]
            i+=1
        j+=1
    a[lo],a[i-1] = a[i-1],a[lo]
    return i-1
        

def quick_sort(a,hi,lo):
    if hi <=lo:
        return
    p = partition(a,hi,lo)
    quick_sort(a,p-1,lo)
    quick_sort(a,hi,p+1)
    
if __name__ == '__main__':
    a=[45,32,12,89,90,76,65]
    quick_sort(a, len(a)-1, 0)
    print a