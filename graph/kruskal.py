class Graph:
    def __init__(self, nodes):
        self.verticles = nodes
        self.graph = []

    def add_edge(self, node_1, node_2, weight):
        self.graph.append([node_1, node_2, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union_find(self, parent, rank, x,y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key = lambda x: x[2])
        parent = []
        rank = []
        for verticle in range(self.verticles):
            parent.append(verticle)
            rank.append(0)

        while e < self.verticles - 1:
            node_1, node_2, weight = self.graph[i]
            i = i + 1
            x = self.find(parent, node_1)
            y = self.find(parent, node_2)
            if x != y:
                e = e + 1
                result.append([node_1, node_2, weight])
                self.union_find(parent, rank, x, y)
        
        for node_1, node_2, weight in result:
            print("%d - %d: %d" % (node_1, node_2, weight))

# initialize graph
graph = Graph(6)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 2)
graph.add_edge(1, 0, 4)
graph.add_edge(2, 0, 4)
graph.add_edge(2, 1, 2)
graph.add_edge(2, 3, 3)
graph.add_edge(2, 5, 2)
graph.add_edge(2, 4, 4)
graph.add_edge(3, 2, 3)
graph.add_edge(3, 4, 3)
graph.add_edge(4, 2, 4)
graph.add_edge(4, 3, 3)
graph.add_edge(5, 2, 2)
graph.add_edge(5, 4, 3)

# do Kruskal
graph.kruskal()