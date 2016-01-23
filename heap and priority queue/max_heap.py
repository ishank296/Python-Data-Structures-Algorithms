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


def extract_max(arr):
	max_elem = arr[0]
	arr[0],arr[-1] = arr[-1],arr[0]
	arr.pop()
	max_heapify(arr,0)
	return max_elem        

def build_maxheap(arr):
    mid = len(arr)/2
    for i in xrange(mid,-1,-1):
        max_heapify(arr,i)
    
        
Arr=[1,2,3,4,5,6,7,8,9]
build_maxheap(Arr)

print Arr
print extract_max(Arr)
print extract_max(Arr)
print extract_max(Arr)
print extract_max(Arr)


print Arr