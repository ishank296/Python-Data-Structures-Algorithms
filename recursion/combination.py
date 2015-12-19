def combination(n,k):
    if (n == k or k == 0):
        return 1
    else:
        return combination(n-1,k) + combination(n-1,k-1)

        