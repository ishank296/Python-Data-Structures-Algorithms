def current_avg(prev_avg,n,k):
    return (prev_avg*n + k)/float(n+1)
    

def streamAvg(arr):
    prev_avg=0.0
    for i in range(len(arr)):
        prev_avg= current_avg(prev_avg,i,arr[i])
        print prev_avg
        

streamAvg([23,12,34,65,78])
    