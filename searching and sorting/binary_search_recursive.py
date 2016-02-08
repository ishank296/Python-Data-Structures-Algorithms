'''
Binary Search

1. Divide : compare x with middle element
2. Conquer : recurse in one subarray
3. Combine : trivial
'''
import time
def binary_search(arr,start,end,k):
    if  start > end:
        return 'Value Not Found'
    print start,end
    mid = (start + end)/2
    time.sleep(1)
    if arr[mid] == k:
        return mid
    elif arr[mid] > k :
        return binary_search(arr,start,mid-1,k)
    else:
        return binary_search(arr,mid+1,end,k)

if __name__ == '__main__':
   print binary_search([2,5,8,90,123,567,569,789,999,1234],0,9,90) 
   print binary_search([2,5,8,90,123,567,569,789,999,1234],0,9,1)