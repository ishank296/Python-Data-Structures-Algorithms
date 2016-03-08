import Queue

class Graph(object):

    def __init__(self,v):
        self.Vertices = v
        self.adj_list = [list() for i in range(v)]


    def addEdge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)


    def dfs(self,s):
        visited = [False for i in range(self.Vertices)]
        self.dfsUtil(s,visited)

    def dfsUtil(self,s,visited):
        visited[s] = True
        print s
        for i in self.adj_list[s]:
            if (not visited[i]):
                self.dfsUtil(i,visited)


if __name__ == '__main__':
    g = Graph(10)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,4)
    g.addEdge(4,5)
    g.addEdge(2,6)
    g.addEdge(2,3)
    g.addEdge(3,7)
    g.addEdge(0,8)
    g.addEdge(7,9)

    g.dfs(0)
