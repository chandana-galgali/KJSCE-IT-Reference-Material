# Input format
# First line: Three integers n (the number of islands), m (the number of one-way bridges), and r (the index of the island you are initially on)
# Next m lines: Two integers ui and vi representing a one-way bridge from island ui to vi.
# Output format
# Print the index of the island that you are most likely to get stuck on. If there are multiple islands, then print them in the increasing order of indices (space separated values in a single line).

# 5 7 1
# 1 2
# 1 3
# 1 4
# 1 5
# 2 4
# 2 5
# 3 4

from collections import defaultdict
n, m, r = map(int,input().split())
edges = []
for i in range(0, m):
    ui, vi =  map(int, input().split())
    edges.append((ui, vi))
graph = defaultdict(list)
stuck_probability = defaultdict(lambda: 0)
for u, v in edges:
    graph[u].append(v)
def calculate_probabilities(node, probability):
    if len(graph[node]) == 0:
        stuck_probability[node] += probability
    else:
        next_prob = probability / len(graph[node])
        for next_node in graph[node]:
            calculate_probabilities(next_node, next_prob)
calculate_probabilities(r, 1)
max_prob = max(stuck_probability.values())
precision_limit = 1e-9
most_probable_sinks = [node for node, prob in stuck_probability.items()
                       if abs(prob - max_prob) < precision_limit]
most_probable_sinks.sort()
print(" ".join(map(str, most_probable_sinks)))