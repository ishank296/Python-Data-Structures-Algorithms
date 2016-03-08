#return left most(first) occurence of k
def binary_search_left(arr,k):
    start = 0
    end = len(arr)-1
    result = -1
    while (start<=end):
        mid = (start+end)/2
        if k == arr[mid]:
            result = mid   # if k found, update value of result and continue serarch in left part
            end = mid-1
        elif k < arr[mid]: # if k less than mid element, search in elements before mid element
            end = mid-1
        else:
            start = mid+1   # if k greater than mid element, search in elements after mid element
    return result




#return right most(last) occurence of k
def binary_search_right(arr,k):
    start = 0
    end = len(arr)-1
    result = -1
    while (start<=end):
        mid = (start+end)/2
        if k == arr[mid]:
            result = mid   # if k found, update value of result and continue serarch in right part
            start = mid+1
        elif k < arr[mid]: # if k less than mid element, search in elements before mid element
            end = mid-1
        else:
            start = mid+1   # if k greater than mid element, search in elements after mid element
    return result




if __name__ == '__main__':
    arr =  [2,2,2,4,4,7,7,9,9,12,23,23,44,56,78,78,89,89]
    print binary_search_left(arr,2)
    print binary_search_left(arr,7)
    print binary_search_left(arr,23)
    print binary_search_left(arr,78)
    print "************************"
    print binary_search_right(arr,2)
    print binary_search_right(arr,7)
    print binary_search_right(arr,23)
    print binary_search_right(arr,78)
