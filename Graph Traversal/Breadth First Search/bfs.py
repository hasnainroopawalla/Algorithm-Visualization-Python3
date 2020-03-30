
# graph = {'A': ['B',  'E'],
#          'B': ['A','D', 'E'],
#          'C': ['A', 'F', 'G'],
#          'D': ['B'],
#          'E': ['A', 'B','D'],
#          'F': ['C'],
#          'G': ['C']}

def bfs_shortest_path(graph, start, goal):

    explored = []
    queue = [[start]]
 
    if start == goal:
        return "Start = goal"
 
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            
            neighbours = graph[node]
            #print('node',node)
            
            for neighbour in neighbours:
                #print(neighbour)
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path
 
            explored.append(node)
 
    return "No route found"
 
