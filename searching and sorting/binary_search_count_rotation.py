# Count number of times a sorted array is rotated
# No of rotation of sorted array = index of minimum element in the array

def FindRotationCount(arr):
    start = 0
    end  = len(arr)-1
    while (start<=end):
        if (arr[start]<=arr[end]): # if arr is already sorted, then start is minimum element
            return start
        else:
            mid = (start+end)/2
            nextelem = (mid + 1) % len(arr) #calculate element next to mid
            prevelem = (mid + len(arr) - 1) % len(arr) #calculate element previous to mid
            if arr[nextelem] >= arr[mid] and arr[prevelem] >= arr[mid]: #if mid element is lower than both previous and next
                return mid
            elif (arr[mid]<=arr[end]): # if right part is sorted, discard right partition
                end = mid - 1
            elif (arr[mid]>= arr[start]): # if left part is sorted, discard left partition
                start = mid + 1
    return -1

if __name__ == '__main__':
    arr = [12,34,45,65,2,3,5,8,10]
    print FindRotationCount(arr)
