import timeit
import time
# start = timeit.timeit()


# end = timeit.timeit()

# result = start - end
# print(result)


# kruskals instance without functions, classes maybe at least one! a for loop is a must need
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

# print(edges)

# two points and the weight at the end

sorted_edges = [
    (2, 3, 4),
    (0, 3, 5),
    (0, 3, 6),
    (0, 1, 10),
    (1, 3, 15),
]

# print(sorted_edges)

# intialize the sets (one for each vertex)
sets = [{0}, {1}, {2}, {3}]

# print(sets[2])
# print(sets[3])
# manually apply kruskals algorithm
mst = []

# process the first edge (2, 3, 4)
sets[2] = sets[2].union(sets[3])
# print(sets[2])

# 3 takes the place of 2 here
# a swap
# but 3 takes {2, 3} this time
sets[3] = sets[2]

mst.append((2, 3, 4))

# log the mst to check what the state of it is until now
# print(mst)


# process the second edge (0, 3, 5)
sets[0] = sets[0].union(sets[3])
# print(sets[0])
sets[3] = sets[0]
mst.append((0, 3, 5))

# print(mst)

# process the third edge (0, 2, 6) -> skip because it creates a cycle

# process the fourth edge (0, 1, 0)
sets[0] = sets[0].union(sets[1])
sets[1] = sets[0]
mst.append((0, 1, 0))

# the remaining edge (1, 3, 15) is not needed as the mst is complete
print(mst)


# diagram with weights

# 1--(10)--0
#      |   
#     (5)
#      |   
#      3
#      | 
#     (4)
#      | 
#      2

# shown in a table

# Vertex 1 | Vertex 2 | Weight
# ---------------------------
#     2    |    3     |   4
#     0    |    3     |   5
#     0    |    1     |   10


