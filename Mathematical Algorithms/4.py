'''
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] ==>n=15
[1,3,5,7,9,11,13,15] ==>counter=2,next_pos=8
[1,3,7,9,13,15] ==>counter=3, next_pos=6 
[1,3,7,13,15] ==>counter=4, next_pos=5
[1,3,7,13] ==>counter=5, next_pos= __
'''

def isLucky(n,counter=2):
    next_pos = n
    if n < counter:
        return True
    elif n % counter ==0:
        return False
    next_pos = next_pos - next_pos/counter
    counter= counter+1
    return isLucky(next_pos,counter)

print isLucky(15)
        
    
    
    