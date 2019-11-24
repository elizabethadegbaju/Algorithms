from collections import defaultdict
import time


class Graph:

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s, goal):
        start = time.time()
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            if s in goal:
                end = time.time()
                print(end - start, " seconds")
                return 0
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        end = time.time()
        print(end - start, " seconds")


g = Graph()
g.addEdge(0, 6)
g.addEdge(0, 3)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(6, 9)
g.addEdge(3, 7)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(7, 9)
g.addEdge(4, 8)
g.addEdge(5, 11)
g.addEdge(9, 10)
g.addEdge(8, 10)
g.addEdge(10, 0)
g.addEdge(11, 0)

print("Following is Breadth First Traversal"
      " (starting from vertex 0)")

goal = [8, 9, 10, 11]
g.BFS(0, goal)