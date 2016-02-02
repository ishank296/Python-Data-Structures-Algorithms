from collections import Counter

'''
dict subclass for counting hashable objects.Elements are counted from an iterable or initialized from another mapping

Counter objects have dictionary interface except that they return a zero count from missing items insted of raising a KeyError
'''

c  = Counter()
c1 = Counter('this is a test')
c2 = Counter({'red':4,'blue':20})

c3 = Counter(a=4,b=3,c=6,d=9)
c4 = Counter(a=9,b=8,c=2,d=12)



print c1.most_common(4)
print list(c2.elements())
c3.subtract(c4)
print c3