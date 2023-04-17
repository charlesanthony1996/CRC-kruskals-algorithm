import time
import timeit
import random

# A -- 10 -- B -- 20 -- C
# |         |         |
# 30        50        40
# |         |         |
# D -- 10 -- E ------- F


# the example is a road network
#  ABCDEF are cities and the weights represent distances

road_network = {
    'A': [('B', 10), ('D', 30)],
    'B': [('A', 10), ('C', 20), ('E', 50)],
    'C': [('B', 20), ('F', 40)],
    'D': [('A', 30), ('E', 10)],
    'E': [('B', 50), ('D', 10), ('F', 60)],
    'F': [('C', 40), ('E', 60)]
}

print(road_network)

import heapq

def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = { start: 0}
    previous_vertices = {start:None}


    while queue:
        pass
