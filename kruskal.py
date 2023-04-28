import time
import timeit

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return f"({self.src}, {self.dest}, {self.weight})"



class Graph:
    def __init__(self, vertices):
        pass


    def add_edge(self, src, dst, weight):
        pass

    def find(self, parent, i):
        pass

    