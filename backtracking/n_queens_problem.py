class NQueens(object):

    def __init__(self,N):
        self.solution = [[0 for j in range(N)] for i in range(N)]
        self.solve(N)
    
    def issafe(self,row,col):
        #check backwards horizontally
        for i in range(col):
            if self.solution[row][i] ==1:
                return False
            
        #check upper diagonal
        r,c=row,col
        while r >= 0  and c >= 0 :
            if self.solution[r][c] ==1:
                return False
            r=r-1
            c=c-1
        
        #check lower diagonal
        r,c=row,col
        while r < len(self.solution) and c >= 0:
            if self.solution[r][c] ==1:
                return False
            r=r+1
            c=c-1
        return True
            

    
    def solve(self,N):
        if self.placeQueen(0,N):
            for i in range(N):
                    print self.solution[i]
        else:
            print "No solution exists"
    
    def placeQueen(self,col,N):
        if (col == N):
            return True
        else:
            for row in range(N):
                if self.issafe(row,col):
                    self.solution[row][col] = 1
                    if self.placeQueen(col+1,N) : 
                        return True
 
                self.solution[row][col] = 0
            
            return False


p=NQueens(8)
       