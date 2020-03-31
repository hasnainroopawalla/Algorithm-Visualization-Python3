visited = []

def dfs_shortest_path(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs_shortest_path(visited, graph, neighbour)
        if(len(visited)==len(graph)):
            return visited

