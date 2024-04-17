import heapq
# n = number of nodes
# edges: list of [source, destination, weight]
# source node = node where we start
def dijkstra(n, edges, source_node):
    # create adjacency list
    adjacency_list = {}
    for i in range(n):
        adjacency_list[i] = []
    
    # unpack the edges list as src, dst, weight vars
    for src, dst, weight in edges:
        adjacency_list[src].append([dst, weight])

    result = {} # map node to dist of shorted path
    minHeap = [(0, source_node)] # weight to reach source node is 0
    while minHeap:
        # unpack values from heap
        w1, n1 = heapq.heappop(minHeap)
        # if n1 already in result -> skip
        if n1 in result:
            continue
        
        result[n1] = w1
        # go through neighbours of n1
        for n2, w2 in adjacency_list[n1]:
            if n2 not in result:
                heapq.heappush(minHeap, [w1 + w2, n2])

    # what if there are non visited nodes?
    # assign them with -1 distance
    for i in range(n):
        if i not in result:
            result[i] = -1
    return result


sample_n = 5
sample_edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
sample_source_node = 0

r = dijkstra(sample_n, sample_edges, sample_source_node)
print(r)