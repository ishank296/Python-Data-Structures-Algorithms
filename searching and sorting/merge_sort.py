'''
Merge Sort:  A[a1,a2,......,an]

1.) if A.length = 1: 
    done
2.) Recursive call sort
    merge_sort(A[a1,a2,.....an/2])
    merge_sort(A[an/2,an/2+1,an/2+2.....an])
3.) Merge two sorted lists
'''

def merge(arr1,arr2):
    result = []
    while len(arr1) and len(arr2):
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    if len(arr1) == 0:
        result.extend(arr2)
    else:
        result.extend(arr1)
    return result

def merge_sort(arr):
    if len(arr) ==1:
        return arr
    else:
        l_arr = merge_sort(arr[:len(arr)/2])
        r_arr = merge_sort(arr[len(arr)/2:])
        r= merge(l_arr,r_arr)
        return r
if __name__ =='__main__':
    print merge_sort([2,4,56,78,87,98,1,5,8,9,109,234])
