'''
Given an array of n elements, Find three elements in the array such that their sum is equal to given number k
'''


def three_elements_with_sum(arr,k):
    arr.sort()
    for i in range(len(arr)):
        low = i+1
        high = len(arr)-1
        while (low<high):
            crsum = arr[i] + arr[low]+ arr[high]
            if crsum == k:
                return arr[i], arr[low], arr[high]
            elif crsum > k:
                high = high -1
            else:
                low = low + 1
    return False

if __name__ == '__main__':
    print three_elements_with_sum([2,35,67,98,56,43,7,3,9],45)
