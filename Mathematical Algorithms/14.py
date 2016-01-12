

def sieve_of_eratosthenes(n):
    prime = [True]*n
    i = 2
    while(i*i < n):
        if prime[i] ==True:
            for j in range(2*i,n,i):
                prime[j]=False
        i=i+1
    for k in range(2,n):
        if prime[k] ==True: print k


sieve_of_eratosthenes(100)
