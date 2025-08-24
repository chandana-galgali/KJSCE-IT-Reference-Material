from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def bfs(self, start, goal):
        visited = set()
        queue = deque([start])
        path_dict = {start: None}
        while queue:
            node = queue.popleft()
            if node == goal:
                path = self._reconstruct_path(start, goal, path_dict)
                print("Visited nodes: ", visited)
                print("Fringe: ", [n for n in queue])
                print("Path traversed: ", path)
                return path
            if node not in visited:
                visited.add(node)
                print("Visited nodes: ", visited)
                print("Fringe: ", [n for n in queue])
                for neighbor in self.graph[node]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
                        path_dict[neighbor] = node
        print("No path found!")
        return None
    def _reconstruct_path(self, start, goal, path_dict):
        path = []
        while goal is not None:
            path.append(goal)
            goal = path_dict[goal]
        return list(reversed(path))
g = Graph()
num_edges = int(input("Enter the number of edges: "))
print("Enter the edges in the format 'source destination':")
for _ in range(num_edges):
    u, v = input().split()
    g.add_edge(u, v)
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
g.bfs(start_node, goal_node)