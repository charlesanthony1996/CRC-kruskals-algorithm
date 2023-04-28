using System;
using System.IO;
using System.Collections.Generic;

// IEdge is an interface that has basic edge properties
// its basically a contract that forces the class to have certain properties
// this interface could have something else like an id? but doesnt make sense since the
// implementation is at a generic level
// keeps the class locked in and fitted to these three properties
public interface IEdge
{
    int Vertex1 { get; }
    int Vertex2 { get; }
    int Weight { get; }
}

// The Edge class represents edges in a graph and helps with sorting
public class Edge: IEdge, IComparable<Edge>
{
    public int Vertex1{ get; }
    public int Vertex2{ get; }
    public int Weight { get; }

    // the constructor initializes edge with two vertices and a weight
    public Edge(int vertex1, int vertex2, int weight)
    {
        Vertex1 = vertex1;
        Vertex2 = vertex2;
        Weight = weight;
    }

    // CompareTo is inbuilt and helps with sorting edges by weight
    public int CompareTo(Edge other)
    {
        return Weight.CompareTo(other.Weight);
    }
}

// the UnionFind data structure helps us track connected components
public class UnionFind
{
    private int[] parent;
    private int[] rank;

    // the class constructor that initializes arrays for parents and rank
    public UnionFind(int size)
    {
        parent = new int[size];
        rank = new int[size];


        for(int i = 0; i < size; i++)
        {
            parent[i] = i;
            rank[i] = 0;
        }
    }

    // the find method helps us find the root of a given vertex
    public int Find(int vertex)
    {
        if(parent[vertex] != vertex)
        {
            parent[vertex] = Find(parent[vertex]);
        }

        return parent[vertex];
    }

    // union tries to merge two sets, returns true if successful
    public bool Union(int vertex1, int vertex2)
    {
        int root1 = Find(vertex1);
        int root2 = Find(vertex2);

        if(root1 == root2)
        {
            return false;
        }

        if (rank[root1] > rank[root2])
        {
            parent[root2] = root1;
        }

        else {
            parent[root1] = root2;

            if(rank[root1]== rank[root2])
            {
                rank[root2]++;

            }
        }

        return true;
    }
}

// kruskal alogrithm is where the algorithm happens to find the minimum spanning tree
public class KruskalAlgorithm
{
    public static List<Edge> Execute(List<Edge> edges, int vertexCount)
    {
        // sorting edges by weight
        edges.Sort();
        // initialize an instance of the UnionFind class here
        UnionFind uf = new UnionFind(vertexCount);

        // prepare an empty list for the mst
        List<Edge> mst = new List<Edge>();

        // go through each and every edge and try to merge connected components
        foreach(var edge in edges)
        {
            if(uf.Union(edge.Vertex1, edge.Vertex2))
            {
                // adding the edge to the empty list here
                mst.Add(edge);
            }
        }
        // returning the list
        return mst;
    }
}


// the main class program where we read input , run the algorithm and write the output for it
class Program
{
    static void Main(string[] args)
    {
        string inputFile = "input.txt";
        string outputFile = "output.txt";
        int vertexCount;

        List<Edge> edges = new List<Edge>();

        // read input from file
        using (StreamReader sr = new StreamReader(inputFile))
        {
            vertexCount = int.Parse(sr.ReadLine());

            string line;
            while ((line = sr.ReadLine()) != null)
            {
                string[] edgeData = line.Split(' ');
                int v1 = int.Parse(edgeData[0]);
                int v2 = int.Parse(edgeData[1]);
                int weight = int.Parse(edgeData[2]);

                // add edges to the list
                edges.Add(new Edge(v1, v2, weight));
            }
        }

        // run the kruskals algorithm to get the minimum spanning tree
        List<Edge> mst = KruskalAlgorithm.Execute(edges, vertexCount);

        // write the minimum spanning tree to the output file
        using (StreamWriter sw = new StreamWriter(outputFile))
        {
            int totalWeight = 0;
            foreach(var edge in mst)
            {
                totalWeight += edge.Weight;
                sw.WriteLine($"{edge.Vertex1} {edge.Vertex2} {edge.Weight}");
            }
            // output the total weight of the minimum spanning tree
            sw.WriteLine($"Total weight: {totalWeight}");
        }
    }
}