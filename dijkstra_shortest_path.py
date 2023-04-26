import networkx as nx


# create an empty graph
G = nx.Graph()


# add nodes (intersections) to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")


# add edges (roads) with weights (distances) to the graph
G.add_edge("A", "B", weight= 5)
G.add_edge("A", "C", weight= 7)
G.add_edge("B", "C", weight= 3)
G.add_edge("B", "D", weight= 3)
G.add_edge("C", "D", weight= 5)
G.add_edge("C", "E", weight= 7)
G.add_edge("D", "E", weight= 1)


shortest_path = nx.dijkstra_path(G, "A", "E")

print("Shortest path from A to E: ", shortest_path)