edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4),
]

# print(edges)

# number of vertices or points
# its always n - 1 here , otherwise it will be a cycle
num_vertices = 4
# sort the edges by weight
sorted_edges = sorted(edges, key=lambda edge: edge[2])

# print(sorted_edges)


# union-find data structure 
parent = [i for i in range(num_vertices)]
# print(parent)
rank = [0] * num_vertices

# find method
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# union method
def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y]= root_x
            rank[root_x] += 1


# kruskals algorithm
mst = []
for edge in sorted_edges:
    u, v, w = edge
    if find(u) != find(v):
        mst.append(edge)
        union(u, v)


# print()
print(mst)