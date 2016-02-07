'''
number of inversions = number of pairs (i,j) with i<j and Arr[i] > Arr[j]

e.g [1,3,5,2,4,6]
inversions : (3,2),(5,2),(5,4)

largest possible number of inversion in array of size n : n(n-1)/2

Number of Inversions: Divide and Conquer
   let (i,j) be a inversion with i<j and Arr[i]>Arr[j]
   Left inversion if both i,j <= n/2
   Right inversion if both i,j > n/2
   Split inversion if i <= n/2 < j
   
   
High level Algo:
Count(array A,length n):
    if n==1 : return 0
    else: 
        x = Count(A[0:n/2],n/2)
        y = Count(A[n/2:],n/2)
        t = CountSplit(A,n)
    
    return x+y+t
    
    
    
 
'''