// how kruskal works
// the core concept of this algorithm is to sort all the edges of the graph by weight and thats the last
// number of the tuple.the first two being the vertices or points.
// and then you try to add them to get the minimum spanning tree/value.
// this is while ensuring that no cycles have been formed
// to understand what cycles (its when vertices fully connect) refer to the python file simple_graph_algorithm.py

const edges = [
    [0, 1, 1],
    [0, 2, 2],
    [1, 2, 3],
    [1, 3, 4],
    [2, 3, 5]
]

// output the edges
// console.log(edges)

// draw the viz of the graph here

// sorting the edges by weight
edges.sort((a, b) => a[2] - b[2])

// assuming there are 4 vertices in the graph
// its always n- 1 here to get the number of vertices -> weights - 1 = gives you the # of vertices
// you could draw the graph and see for yourself as well
const numVertices = 4

const parents = []

for (let i = 0; i < numVertices; i++)
{
    parents.push(i)
}


// the find function is to find the root(parent) of a given vertex
function find(u) {
    // if the parent of the vertex is itself, return the vertex
    if(parents[u] === u) {
        return u
    }
    // otherwise , recursively find the parent of the vertex
    return find(parents[u])
}

// 
function union(u, v) {
    // find the parents of the both vertices u and v
    const parentU = find(u)
    const parentV = find(v)

    // if the parents are different , perform the union operation
    if(parentU != parentV) {
        // make the parent of vertex v the parent of the vertex U
        parents[parentV] = parentU
        // return true to indicate a successful union operation
        return true
    }
    // if the parents are the same output false to indicate that no kind of union has takne place
    return false
}


// initialize an empty array
const mst = []

// iterate through the edges of the array
for(let i = 0; i < edges.length; i++) {
    // destructure the source, target and weight of the current edge
    const [source, target, weight] = edges[i]

    // perform the union operation for the source and target vertices
    if(union(source, target)) {
        // if the union is successful , add the edge to the mst here
        mst.push([source, target, weight])
    }
}

// output the minimum spanning tree here
console.log(mst)






