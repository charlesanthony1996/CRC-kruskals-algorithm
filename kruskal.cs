using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;


// defining the edge structure
// this can be an interface
// check the kruskal with class program
struct Edge
{
    public int Source;
    public int Destination;
    public int Weight;
}

// main kruskals algorithm
class KruskalsAlgorithm
{
    static int Find(int[] parent, int i)
    {
        if (parent[i] == -1)
            return i;
        return Find(parent, parent[i]);
    }

    static void Union(int[] parent, int x, int y)
    {
        int xset = Find(parent, x);
        int yset = Find(parent, y);
        parent[xset] = yset;
    }

    static void Kruskal(Edge[] edges, int V)
    {
        // sort the edges by their weight in ascending order
        Array.Sort(edges, (a, b) => a.Weight.CompareTo(b.Weight));

        // initialize the parent array for the disjoint set
        int[] parent = new int[V];
        for (int i = 0; i < V; ++i)
            parent[i] = -1;

        // initialize the result list to store the mst edges
        List<Edge> result = new List<Edge>();

        // intialize the variables for counting edges and the current edge index
        int e = 0;
        int index = 0;

        // keep adding edges until we have V - 1 edges in the result
        while (e < V - 1)
        {
            // get the next edge in the sorted array
            Edge nextEdge = edges[index++];

            // find the parents of the source and destination vertices
            int x = Find(parent, nextEdge.Source);
            int y = Find(parent, nextEdge.Destination);

            // if the src and destination dont share the same parent or root
            // add the edge to the result and merge the sets
            // adding any edge here would not create a cycle or a closed loop
            // find gets the root of the edge
            // and union merges them

            // if the source and destination have the same parent or root?
            // that means the edge is the connection to the closed loop and must not be added

            // check our input file

            // 4
            // 0 1 2
            // 1 2 3
            // 2 3 1
            // 3 0 4

            // 4 vertices and the edges

            // the normal output without the if function below would be

            // 2 - 3: 1
            // 0 - 1: 2
            // 1 - 2: 3
            // 3 - 0: 4

            // its sorted by the weight
            // but the last edge cannot be added since it creates a cycle
            // so after the code snippet below it gets removed
            
            // the corrected output

            // 2 - 3: 1
            // 0 - 1: 2
            // 1 - 2: 3


            if (x != y)
            {
                result.Add(nextEdge);
                Union(parent, x, y);
                e++;
            }
        }

        // write the sorted edge and no cycle , final result to the output.txt file
        // do some stream writing excercises to get familiar with file reading and writing manipulation
        using StreamWriter outputFile = new StreamWriter("output.txt");
        foreach (Edge edge in result)
        {
            outputFile.WriteLine($"{edge.Source} - {edge.Destination}: {edge.Weight}");
        }
    }

    // the main function that reads the input file , uses kruskals and creates/writes the output file
    static void Main(string[] args)
    {
        // initialize the list of edges
        // do we need a list? check for arrays
        List<Edge> edgesList = new List<Edge>();

        // initialize the numbers variable
        int vertices = 0;

        // reading function for the input.txt file
        using (StreamReader inputFile = new StreamReader("input.txt"))
        {

            string line;
            vertices = int.Parse(inputFile.ReadLine());

            // reading operation from IO
            // do some seperate exercises with system.io to get familiary with file manipulation
            // read the following lines to get the edges and add them to the list
            while ((line = inputFile.ReadLine()) != null)
            {
                // split the line by a space and parse each integer , then create an edge from the parsed data
                int[] edgeData = line.Split().Select(int.Parse).ToArray();
                edgesList.Add(new Edge { Source = edgeData[0], Destination = edgeData[1], Weight = edgeData[2] });
            }
        }

        // convert the list of edges to an array?
        // but why?

        Edge[] edges = edgesList.ToArray();
        
        // call the algorithm function with the array of edges and the number of vertices
        Kruskal(edges, vertices);
    }
}
