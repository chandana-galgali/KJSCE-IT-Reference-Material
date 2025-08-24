def topological_sort(n, edges):
    from collections import defaultdict, deque

    # Graph initialization
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    visited = [False] * (n + 1)
    stack = []
    
    # Building the graph
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Function to perform DFS
    def dfs(v):
        visited[v] = True
        stack.append(v)  # Use stack to hold the current path for cycle detection
        for neighbor in graph[v]:
            if neighbor in stack:  # Cycle detection
                return True
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
        stack.pop()
        result.append(v)  # Append to result if all descendants are processed
        return False
    
    result = []
    
    # Check each node if not already visited
    for v in range(1, n + 1):
        if not visited[v]:
            if dfs(v):
                return "IMPOSSIBLE"  # Cycle detected

    return result[::-1]  # Reverse the result to get the correct topological order

# Sample input directly within the script
n, e = map(int,input().split())
edges = []
for i in range(0, e):
    ui, vi =  map(int, input().split())
    edges.append((ui, vi))
    
# Perform topological sorting
sorted_order = topological_sort(n, edges)
if isinstance(sorted_order, list):
    print(" ".join(map(str, sorted_order)))
else:
    print(sorted_order)
