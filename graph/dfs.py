def dfs(visited, graph, current_node):
    # check if node is not visited yet
    if current_node not in visited:
        visited.add(current_node)
        # traverse node's neighbors
        for neighbor in graph[current_node]:
            dfs(visited=visited, graph=graph, current_node=neighbor)

visited = set()

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

dfs(visited, graph, 'A')
print(visited)