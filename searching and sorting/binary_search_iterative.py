
def binary_search(Arr,k):
    start = 0
    end = len(Arr)-1
    while  (start<=end):
        mid = (start+end)/2
        if Arr[mid] == k:
            return mid
        elif Arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
    return -1

if __name__ == '__main__':
    arr = [2,5,7,9,12,34,67,89]
    print binary_search(arr,12)
    print binary_search(arr,89)
    print binary_search(arr,7)
    print binary_search(arr,121)
