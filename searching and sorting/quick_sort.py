'''
Quick Sort In place sorting

1.) Divide : partition array into subarray with pivot
    select pivot p
    start from i =start, j=start
    loop from j to end
    if A[j]>pivot
    swap A[i] <==> A[j]
2.) Conquer: recurse sort in both subarray
'''


def partition(arr,start,end):
    pivot = arr[start]
    i = start+1

    for k in range(start+1,end+1):
        if pivot > arr[k]:
            arr[i],arr[k] = arr[k],arr[i]
            i = i+1
    
    arr[start],arr[i-1] = arr[i-1],arr[start]
    return i-1

    
def quick_sort(arr,start,end):
    if start > end:
        return
    p = partition(arr,start,end)
    quick_sort(arr,start,p-1)
    quick_sort(arr,p+1,end)

    
a=[45,56,23,12,68,98,67,54,36,22,90]
quick_sort(a,0,len(a)-1)   
print a 