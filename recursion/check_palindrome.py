def check_palindrome(st):
    if len(st) <= 1:
        return True
    else:
        return (st[0]==st[-1] and check_palindrome(st[1:len(st)-1]))

        
