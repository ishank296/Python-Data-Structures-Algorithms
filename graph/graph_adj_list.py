'''Graph Adjecency list implementation '''

class Vertex(object):
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = "white"
        self.predecessor=None
        self.distance = 0
    
    def getPred(self):
        return self.predecessor
        
    def setPred(self,pred):
        self.predecessor = pred
    
    def getColor(self):
        return self.color
    
    def setColor(self,color):
        self.color = color
    
    def getDistance(self):
        return self.distance
    
    def setDistance(self,distance):
        self.distance = distance
    
    def addNeighbour(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getID(self):
        return self.id

    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return str(self.id)+' connected to: '+str([x.id for x in self.connectedTo])
        
        

class Graph(object):
    
    def __init__(self):
        self.vertlist=dict()
        self.numVertices = 0
    
    def addVertex(self,key):
        self.numVertices = self.numVertices+1
        newVertex = Vertex(key)
        self.vertlist[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return  None
            
    def __contains__(self,n):
        return n in self.vertlist
    
    
    def addEdge(self,f,t,cost=0):
        if f not in self.vertlist:
            self.addVertex(f)
        if t not in self.vertlist:
            self.addVertex(t)
        self.vertlist[f].addNeighbour(self.vertlist[t],cost)
    
    def getVertices(self):
        return self.vertlist.keys()
        
    def __iter__(self):
        return iter(self.vertlist.values())
    
    
    
    
    
#g = Graph()
#for i in range(6):
#    g.addVertex(i)



#g.addEdge(0,1,5)
#g.addEdge(0,5,2)
#g.addEdge(1,2,4)
#g.addEdge(2,3,9)
#g.addEdge(3,4,7)
#g.addEdge(3,5,3)
#g.addEdge(4,0,1)
#g.addEdge(5,4,8)
#g.addEdge(5,2,1)



#print g.vertlist
#for v in g:
#    print g.getVertex(v.getID())