from graph import Vertex
from graph import Graph

a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
s = Vertex('S')
g = Vertex('G')

graph = Graph()

graph.add_vertex(a)
graph.add_vertex(b)
graph.add_vertex(c)
graph.add_vertex(d)
graph.add_vertex(s)
graph.add_vertex(g)

graph.add_path(s, a, 2)
graph.add_path(s, b, 3)
graph.add_path(s, d, 5)
graph.add_path(a, c, 4)
graph.add_path(b, d, 4)
graph.add_path(c, d, 1)
graph.add_path(c, g, 2)
graph.add_path(d, g, 5)

def bfs(graph, start, goal):
    queue = [start]
    visited = []
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)
            if current == goal:
                return visited
            neighbours = graph.verteses[current].neighbours
            queue.extend(sorted(neighbours))
    return visited


def dfs(graph, start, goal):
    stack = [start]
    visited = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            if current == goal:
                return visited
            neighbours = graph.verteses[current].neighbours
            stack.extend(sorted(neighbours))
    return visited
        
    


print(bfs(graph, 'S', 'G'))
print(dfs(graph, 'S', 'G'))
