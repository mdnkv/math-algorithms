from collections import deque

def bfs(visited_nodes, start_node, graph):
    # create queue
    queue = deque()
    visited_nodes.add(start_node)
    queue.append(start_node)

    while queue:
        # get current node from queue
        current_node = queue.popleft()
        # get all adjancent nodes of the current node
        for neighbor in graph[current_node]:
            # check if not in result
            if neighbor not in visited_nodes:
                # add to results
                visited_nodes.add(neighbor)
                # add tot queue
                queue.append(neighbor)


graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()
bfs(visited_nodes=visited, start_node='A', graph=graph)
print(visited)