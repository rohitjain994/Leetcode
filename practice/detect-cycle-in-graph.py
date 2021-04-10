# Python program to detect cycle
# in a graph

from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    # Returns true if graph is cyclic else false
    def isdirCyclic(self): 
        visited = [0]*self.V
        def cycle(v):
            visited[v] = 1
            for i in self.graph[v]:
                if visited[i]: return True
                elif cycle(i):
                		return True
            visited[v] = 0
            return False
        for node in range(self.V):
            if not visited[node] and cycle(node):
                return True
        return False

    def isundirCyclic(self): 
        visited = [0]*self.V
        def cycle(v,seen):
            if seen[v] == 2:
                return True
            seen[v] = 1
            for i in self.graph[v]:
                if seen[i]==1:
                    seen[i] = 2
                elif cycle(i,seen):
                		return True
            return False
        for node in range(self.V):
            if not visited[node] and cycle(node,visited):
                return True
        return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
g.addEdge(2, 3)
# g.addEdge(3, 3)
print(g.graph)
if g.isdirCyclic():
	print("Graph has a cycle")
else:
	print("Graph has no cycle")
g.addEdge(1, 0)
g.addEdge(2, 1)
g.addEdge(3, 2)
print(g.graph)
if g.isundirCyclic():
	print("Graph has a cycle")
else:
	print("Graph has no cycle")

# Thanks to Divyanshu Mehta for contributing this code
