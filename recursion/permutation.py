def permutation(sofar,rest):
    if rest == "":
        print sofar
    else:
        for i in range(len(rest)):
            next=sofar+rest[i]
            remaining = rest[:i] + rest[i+1:]
            permutation(next,remaining)

#permutation("","abcd")