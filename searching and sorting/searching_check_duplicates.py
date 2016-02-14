'''
Given an array of n numbers, give an algorithm for checking whether there are any duplicate elements in the array or not
'''


#brute force technique: O(n^2)
def check_duplicate_bruteforce(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


#sort and scan: O(n)
def check_duplicate_sort(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            return True
    return False


#using hashing
def check_duplicate_hashing(arr):
    table =  dict()
    for i in arr:
        if table.get(i) == 1:
            return True
        else:
            table[i] = 1
    return False



if __name__ == '__main__':
    print check_duplicate_bruteforce([1,3,5,3,7,5,8,67,8])
    print check_duplicate_bruteforce([1,3,5,35,7,53,82,67,])
    print check_duplicate_sort([1,3,5,3,7,5,8,67,8])
    print check_duplicate_sort([1,3,5,35,7,53,82,67,])
    print check_duplicate_hashing([1,3,5,3,7,5,8,67,8])
    print check_duplicate_hashing([1,3,5,35,7,53,82,67,])
