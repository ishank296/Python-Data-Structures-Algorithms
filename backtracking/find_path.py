class FindPathMatrix(object):
   
    def __init__(self,N):
        self.solution = [[0 for i in range(N)] for j in range(N)]
        self.N=N
        
    def solve(self,matrix):
        if self.find_path(0,0,matrix,self.N):
            for i in range(self.N):
                print self.solution[i]
        else:
            print "No path found"
    
    def find_path(self,row,column,matrix,N):
        if (row ==N-1 and column == N-1):
            self.solution[row][column] = 1
            return True
        if matrix[row][column] == 0 or self.solution[row][column]==1:
            return False
        else:
            self.solution[row][column] = 1
            if (row+1 < N and self.find_path(row+1,column,matrix,N)): return True
            
            if (column+1 < N and self.find_path(row,column+1,matrix,N)): return True
                        
            if(row - 1 >=0 and self.find_path(row-1,column,matrix,N)): return True
            
            if(column - 1 >=0 and self.find_path(row,column-1,matrix,N)): return True
            
            self.solution[row][column] = 0
            return False


p=FindPathMatrix(5)
p.solve([
        [1,1,1,0,1],
        [1,0,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,0],
        [0,1,1,1,1]
        ])            
            