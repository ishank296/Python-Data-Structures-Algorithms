import Queue
from graph_adj_list import Graph,Vertex
def bfs(g,start):
    
    vertQueue = Queue.Queue(100)
    vertQueue.put(start)
    
    while (not vertQueue.empty()):
        currentVert = vertQueue.get()
        print currentVert
        for neighbour in currentVert.getConnections():
            if neighbour.getColor() == 'white':
                neighbour.setColor('grey')
                neighbour.setDistance(currentVert.getDistance()+1)
                neighbour.setPred(currentVert)
                vertQueue.put(neighbour)
        currentVert.setColor('black') 
     

        
g = Graph()
for i in range(8):
    g.addVertex(i)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(4,5,1)
g.addEdge(5,6,1)
g.addEdge(6,2,1)
g.addEdge(6,7,1)    

    
bfs(g,g.getVertex(0))


    
