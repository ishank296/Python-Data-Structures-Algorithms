def find_prime(n):
    primes = [1]*n
    primes[0]=0
    primes[1]=0
    for i in range(2,n):
        if primes[i] ==1:
            for j in range(2,n):
                primes[i*j] = 0
