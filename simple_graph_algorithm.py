graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
}

vertex1 = 0
vertex2 = 1

# check if vertex1 and vertex2 are directly connected
# if vertex2 in graph[vertex1]:
#     print("Vertex1", vertex1 , "and vertex" , vertex2, "are directly connected")
# else:
#     print("Vertex", vertex1, "and vertex", vertex2, "are not directly connected")


# 0 -- 1
# |    |
# |    |
# 2    3

# next example

# simple undirected, and weighted graph
# undirected graphs no need for directions
# syntax to follow -> (0, 1, 4) -> the first two are coords or edges, , 4 being the vertex

weighted_graph = {
    0: [(1, 4), (2, 2)],
    1: [(0, 4), (3, 3)],
    2: [(0, 2)],
    3: [(1, 3)]
}
#
# print(weighted_graph)



vertex1 = 0
vertex2 = 1

# check if vertex1 and vertex2 are directly connected
# if vertex2 in [neighbor[0] for neighbor in weighted_graph[vertex1]]:
#     print("Vertex", vertex1 , "and vertex", vertex2, " are directly connected")

# else:
#     print("vertex", vertex1, "and vertex" , vertex2, 'are not directly connected')


# the dfs algorithm is the next example
# a full cycle
# basic example on how to understand it

# graph

graph1 = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 4],
    4: [2, 3]
}

print(graph)


# graph traversal visualization

# 0 -- 1 -- 3
# |         |
# |         |
# 2 --------4


def dfs(graph, vertex, visited = None):
    if visited is None:
        visited = set()

    visited.add(vertex)
    print(vertex, end=" ")


    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

dfs(graph1, 0)







