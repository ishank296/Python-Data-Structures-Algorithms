def min_heapify(arr,i):
    left = 2*i + 1
    right = 2*i + 2
    N = len(arr)-1
    smallest = i
    if (left <= N and arr[left] < arr[smallest]):
        smallest = left
    
    if (right <= N and arr[right] < arr[smallest]):
        smallest = right
    
    if (smallest!=i):
        arr[smallest],arr[i]=arr[i],arr[smallest]
        min_heapify(arr,smallest)


def build_minheap(arr):
    i = len(arr)/2
    while(i >= 0):
        min_heapify(arr,i)
        i = i-1

Arr=[10,9,8,7,6,5,4,3,2,1]
build_minheap(Arr)
print Arr