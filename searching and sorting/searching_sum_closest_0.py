'''
Given an array with both positive and negative numbers. Find two elements such that their sum is closest to 0
'''

def two_elements_with_closestsum_zero(arr):
    arr.sort()
    low = 0
    high = len(arr)-1
    left_min= 0
    right_min = 0
    closest = 1000
    while (low < high):
        cr_sum = arr[low] + arr[high]
        if abs(cr_sum) < closest:
            closest = cr_sum
            right_min,left_min = low,high
        if cr_sum > 0:
            high = high-1
        if cr_sum < 0:
            low = low +1
        if cr_sum == 0:
            break
    return arr[right_min],arr[left_min]


if __name__ == '__main__':
    print two_elements_with_closestsum_zero([1,60,-10,70,-80,85])
