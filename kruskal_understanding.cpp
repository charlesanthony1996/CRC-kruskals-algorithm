#include <iostream>
#include <algorithm>
#include <vector>


// understanding the edge of struct
// its basically the stick that holds the two points at the end and the middle part is the
// distance/weight/ratio that depends on each use case of the alogrithm

using namespace std;

struct Edge {
    int u;
    int v;
    int weight;

    bool operator<(Edge const& other) {
        return weight < other.weight;
    }
};


int main() {
    // create a few edge instances
    


}