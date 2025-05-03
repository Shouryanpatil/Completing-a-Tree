def count_components(n, edges):
    from collections import defaultdict

    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    components = 0
    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node)
            components +=1

    return components

def minimum_edges_to_tree(n, edge_list):
    components = count_components(n, edge_list)
    return components - 1

# Sample input
n = 10
edges = [(1, 2), (2, 8), (4, 10), (5, 9), (6, 10), (7, 9)]
print(minimum_edges_to_tree(n, edges))
