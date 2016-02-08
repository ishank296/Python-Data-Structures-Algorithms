def binary_search(arr,k,searchFirst):
    start = 0
    end = len(arr)-1
    result = -1
    while(start<=end):
        mid = (start+end)/2
        if arr[mid] == k :  # if k found, update value of result variable
            result = mid
            if (searchFirst): # if search for first occurence, continue search in left part of array
                end = mid - 1
            else:
                start  = mid + 1 # if searh for last occurence, continue searh in right part of array
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
    return result

def find_count(arr,k):
    firstIndex = binary_search(arr,k,True)
    lastIndex = binary_search(arr,k,False)
    count_k = lastIndex - firstIndex + 1
    return count_k


if __name__ == '__main__':
    arr = [1,1,1,1,3,3,3,7,7,7,7,12,12,12,12,12,34,34,34,56,78,89,90,90]
    print find_count(arr,1)
    print find_count(arr,3)
    print find_count(arr,90)
    print find_count(arr,89)
