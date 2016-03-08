'''
Given an array of n elements. Find two elements in the array such that their sum is equal to given number k
'''

def two_elements_with_sum(arr,k):
  arr.sort()
  low = 0
  high = len(arr)-1
  while(low < high):
    if (arr[low] + arr[high]) > k:
      high = high-1
    elif (arr[low] + arr[high]) < k:
      low = low + 1
    else:
      return arr[low],arr[high]
  return False


#using hashing
def two_elements_with_sum_hasing(arr,k):
    table = dict()
    for i in arr:
        table[i] = 1
    for i in arr:
        if table.get(k-i)==1:
            return i,k-i
    return False


if __name__ == '__main__':
    print two_elements_with_sum([2,4,67,5,9,23,45,78,16],28)
    print two_elements_with_sum_hasing([2,4,67,5,9,23,45,78,16],72)
