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
    #build heap
    mid = len(arr)/ 2
    for i in range(mid,-1,-1):
        max_heapify(arr,i,len(arr)-1)

    #heap sort
    for i in range(len(arr)-1,-1,-1):
        arr[0],arr[i]=arr[i],arr[0]
        max_heapify(arr,0,i-1)

a = [23,12,45,76,64,98,60,89]
heap_sort(a)
print a 