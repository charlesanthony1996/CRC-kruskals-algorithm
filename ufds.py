class UFDS:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x == self.parent[x]:
            return x
        # recursive operation here
        # return the root till you keep finding it
        return self.find(self.parent[x])

    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        # checks if the two roots or parents are the different or not
        # if not it makes the parent_q under the parent_p so the parent_p becomes the main root
        if parent_p != parent_q:
            self.parent[parent_p] = parent_q


# Example usage:
if __name__ == "__main__":
    # range is 4 elements
    # why does n = 3 put it out of range?
    # since the parent array will have numbers or indices from 0 to 2, its always n - 1 here
    n = 4

    # creating an instance of the main class
    ufds = UFDS(n)

    # Check the initial state
    # every element is in its own set

    for i in range(n):
        print(f"Element {i} belongs to set {ufds.find(i)}")

    # Perform some union operations:
    ufds.union(0, 1)
    ufds.union(2, 3)
    ufds.union(0, 2)

    print("After performing union operations:")
    for i in range(n):
        print(f"Element {i} belongs to set {ufds.find(i)}")

# This is half of the algorithm as i understood it