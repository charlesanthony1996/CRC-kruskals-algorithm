#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// define a struct for the edge
typedef struct {
    int source;
    int target;
    int weight;
} Edge;

// comparator function for sorting edges by weight using qsort
int compare_edges(const void*a, const void *b) {
    Edge* edge_a = (Edge*)a;
    Edge* edge_b = (Edge*)b;

    return edge_a -> weight - edge_b -> weight;
}

// find function to find the root(parent) of a given vertex
int find(int u, int parents[]) {
    if(parents[u] == u) {
        return u;
    }
    return find(parents[u], parents);
}

// union vertices to connect two vertices and their corresponding vertices
int union_vertices(int u, int v, int parents[]) {
    int parent_u = find(u, parents);
    int parent_v = find(v, parents);

    if(parent_u != parent_v) {
        parents[parent_u] = parent_u;
        return 1;
    }
    return 0;
}

// playground part to understand the functions
// understanding comparing integers for a more clear understanding
int compare_ints(const void*a, const void*b) {
    int int_a = *(int *)a;
    int int_b = *(int *)b;
    
    return int_a - int_b;
}


// comparing floats now, not integers
int compare_floats(const void*a, const void*b) {
    float float_a = *(float *)a;
    float float_b = *(float *)b;

    return float_a - float_b;
}

// comparing strings here
int compare_strings(const void *a, const void *b) {
    char *str_a = *(char **)a;
    char *str_b = *(char **)b;

    return str_a - str_b;
}


// undetstading a struct based object just like in for edges
typedef struct{
    char *name;
    int age;
} Person;

// #include <string.h> has to be used here in order to use strcmp
int compare_person_by_age(const void *a, const void *b) {
    Person *person_a = (Person*)a;
    Person *person_b = (Person*)b;

    return person_a-> age - person_b-> age;
}


int compare_person_by_name(const void *a, const void *b) {
    Person *person_a = (Person*)a;
    Person *person_b = (Person*)b;

    return strcmp(person_a -> name, person_b -> name);
}


// explaining the find function here
// using the find function with a specific node
// is to return the root of the node
// then print it to the console
// learn about disjointed set data structures?
// vertex is singular and vertices is the correct plural form


// what is a disjointed set?
// its basically a union-find data structure
// its two primary operations are find and union

// where find -> given an element , find the subset (or set) that the element belongs to.
// it often gives the root of the set

// where union -> given two elements , merge the subsets they belong to a single subset
// if the elements already belong to the same subset, no changes are made











// int main() {
//     // define the input as an array of edges , where each edge has a source, target and weight
//     Edge edges[] = {
//         {0, 1, 1},
//         {0, 2, 2},
//         {1, 2, 3},
//         {1, 3, 4},
//         {2, 3, 5},
//     };


//     int num_edges = sizeof(edges)/sizeof(Edge);

//     // sort the edges array by the weight of each edge using the qsort function
//     qsort(edges, num_edges, sizeof(Edge), compare_edges);

//     // define a constant for the number of vertices in the graph
//     int num_vertices = 4;

//     // initialize an array to represent the parent of each vertex
//     int parents[num_vertices];

//     // fill the parents array with the initial parent of each vertex(itself)
//     for(int i = 0; i < num_vertices; i++){
//         parents[i] = i;
//     }

//     // initialize an array to represent the mst
//     Edge mst[num_vertices - 1];
//     int mst_count = 0;

//     // iterate through the sorted edges of the array
//     for(int i = 0; i < num_edges && mst_count < num_vertices - 1; i++)
//     {
//         // perform the union operation for the source and target vertices
//         if(union_vertices(edges[i].source , edges[i].target, parents)) {
//             // if the union is successful , add the edge to the minimum spanning tree
//             mst[mst_count++] = edges[i];
//         }
//     }

//     // output the mst
//     printf("Minimum spanning tree: \n");
//     for(int i = 0; i < mst_count; i++) {
//         printf("%d - %d (weight: %d)\n", mst[i].source, mst[i].target, mst[i].weight);
//     }

//     return 0;
// }


// playing around with the functions -> compare_edges, find and union_vertices
int main() {

    // ints
    int num1 = 4;
    int num2 = 3;

    int result = compare_ints(&num1, &num2);
    printf("result: %d\n", result);
    

    // floats
    float num_a = 4;
    float num_b = 1;

    float result1 = compare_floats(&num_a, &num_b);
    printf("Result: %f\n", result1);


    // using the strings example now
    Person alice = {"Alice", 30};
    Person bob = {"Bob", 25};

    int age_comparison_result = compare_person_by_age(&alice, &bob);

    printf("Age comparison result: %d\n", age_comparison_result);

    // find function to return the root of the node
    int parents[] = {0, 0, 2, 2, 4, 4, 6};

    int u = 3;
    int root = find(u, parents);

    printf("Root of the node: %d\n", u, root);

    return 0;
 
}

