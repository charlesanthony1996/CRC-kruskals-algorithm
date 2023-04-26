#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int u;
    int v;
    int weight;

    bool operator<(Edge const & other) {
        return weight < other.weight;
    }
};



int find(vector<int> &parent, int u) {
    if(u == parent[u]) {
        return u;
    }

    return parent[u] = find(parent, parent[u]);
}


void union_sets(vector<int> &parent, vector <int> & rank, int a, int b) {
    a = find(parent, a);
    b = find(parent, b);

    if(a != b) {
        if(rank[a] > rank[b]) {
            swap(a, b);
        }

        parent[b] = a;
        if(rank[a] == rank[b]) {
            rank[a]++;
        }
    }
}



int main() {

    int n;
    int m;
    cout << "Enter the number of vertices and edges: ";

    cin >> n >> m;

    vector<Edge> edges(m);
    cout << "Enter the edges (u, v, weight): " << endl;

    for(int i = 0;i <m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].weight;
    }

    sort(edges.begin(), edges.end());

    vector<int> parent(n);
    vector<int> parent[n, 0];

    





    return 0;
}