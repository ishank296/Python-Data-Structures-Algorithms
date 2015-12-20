class word_matrix(object):
    
    def __init__(self,N):
        self.N=N
        self.solution = [[0 for i in range(N)] for j in range(N)] 
        self.path=0
    
    
    
    def search_word(self,matrix,word):
        for i in range(self.N):
            for j in range(self.N):
                if self.find_word(i,j,matrix,word,0):
                    for k in range(len(self.solution)):
                        print self.solution[k]
                    return
        print "Word Not found in matrix"
        
    
    
    
    def find_word(self,i,j,matrix,word,index):
        if index == len(word)-1:
            self.path+=1
            self.solution[i][j] = self.path
            return True
        else:
            if matrix[i][j] != word[index] or self.solution[i][j] != 0:
                return False
            
            self.path+=1
            self.solution[i][j] = self.path
        
            if (i + 1 < self.N and self.find_word(i+1,j,matrix,word,index+1)): return True
            
            if (j + 1 < self.N and self.find_word(i,j+1,matrix,word,index+1)): return True
            
            if (i + 1 < self.N and j + 1 < N and self.find_word(i+1,j+1,matrix,word,index+1)): return True
            
            if (i - 1 >= 0 and self.find_word(i-1,j,matrix,word,index+1)): return True
            
            if (j - 1 >= 0 and self.find_word(i,j-1,matrix,word,index+1)): return True
            
            if (i - 1 >= 0 and j - 1 >= 0 and self.find_word(i-1,j-1,matrix,word,index+1)): return True
            
            if (i + 1 < self.N and j - 1 >= 0 and self.find_word(i+1,j-1,matrix,word,index+1)): return True
            
            if (i - 1 >=0 and j + 1 < self.N and self.find_word(i-1,j+1),matrix,word,index+1): return True
        
            self.solution[i][j] =0
            self.path-=1
            return False
            
            
p=word_matrix(5)
p.search_word(
[['a','x','l','m','c'],
 ['v','b','q','l','d'],
 ['i','e','z','k','h'],
 ['s','b','y','i','t'],
 ['r','j','f','m','e']],
'kite'
)
            
            
            
        
        
            
            