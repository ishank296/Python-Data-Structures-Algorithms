'''
parent of ith elelment=>     Ar[i/2]
left child of ith element=>  Ar[2*i+1]
right child of ith element=> Ar[2*i+2]
'''

def max_heapify(arr,i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    N = len(arr)-1
    if (left <= N and arr[left] > arr[largest]):
        largest = left

    if (right <=N and arr[right]>arr[largest]):
        largest = right
    
    if (largest!=i):
        arr[i],arr[largest]=arr[largest],arr[i]
        max_heapify(arr,largest)
        

def build_maxheap(arr):
    i = len(arr)/2
    while(i >= 0):
        max_heapify(arr,i)
        i = i-1
        
Arr=[1,2,3,4,5,6,7,8,9]
build_maxheap(Arr)
print Arr