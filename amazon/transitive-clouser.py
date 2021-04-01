class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = collections.defaultdict(list)
        for idx in prerequisites:
            graph[idx[0]].append(idx[1])
        matrix = [[0]*n for i in range(n)]
        def dfs(i,j):
            matrix[i][j]=1
            for idx in graph[j]:
                if matrix[i][idx]==0:
                    dfs(i,idx)
        for i in range(n):
            dfs(i,i)
        res = []
        for query in queries:
            res.append(True if matrix[query[0]][query[1]] else False)
        return res

# Given a directed graph, find out if a vertex v is reachable from another vertex u for all vertex pairs (u, v) in the given graph. Here reachable mean that there is a path from vertex u to v. The reach-ability matrix is called transitive closure of a graph.
# Transitive clouser is reachablity matrix from i to j

Floydwarshall algo :
matrix = graph
for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
