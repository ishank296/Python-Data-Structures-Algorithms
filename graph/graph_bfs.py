import Queue

class Graph(object):

    def __init__(self,v):
        self.Vertices = v
        self.adj_list = [list() for i in range(v)]

    '''
    Add Edge between u and v. For directed graph, add edge from u to v
    For undirected,add edge From u to v and v to u.
    '''
    def addEdge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)



    def bfs(self,s):
        visited = [False for i in range(self.Vertices)]
        q = Queue.Queue()
        visited[s]=True
        q.put(s)
        while(not q.empty()):
            c=q.get()
            print c
            for i in self.adj_list[c]:
                if(not visited[i]):
                    visited[i] =True
                    q.put(i)


if __name__ == '__main__':
    g = Graph(10)
    g.addEdge(1,3)
    g.addEdge(2,5)
    g.addEdge(4,5)
    g.addEdge(5,9)
    g.addEdge(2,6)
    g.addEdge(6,8)
    g.addEdge(0,9)
    g.addEdge(3,7)
    g.addEdge(8,7)
    g.addEdge(1,2)
    g.addEdge(9,2)
    print g.adj_list
    g.bfs(0)
