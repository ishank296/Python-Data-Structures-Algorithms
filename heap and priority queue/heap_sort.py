def max_heapify(arr,i,N):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if (left <= N and arr[left] > arr[largest]):
        largest = left
    if (right <= N and arr[right] > arr[largest]):
        largest = right
    if (largest!=i):
        arr[largest],arr[i]=arr[i],arr[largest]
        max_heapify(arr,largest,N)

        
def heap_sort(arr):
    n = len(arr)/ 2
    while (n >= 0):
        max_heapify(arr,n,len(arr)-1)
        n = n-1
    i = len(arr)-1
    while(i >= 0):
        arr[0],arr[i]=arr[i],arr[0]
        max_heapify(arr,0,i-1)
        i=i-1
a = [23,12,45,76,64,98,60,89]
heap_sort(a)
print a 