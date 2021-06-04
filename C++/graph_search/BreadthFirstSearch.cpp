#include <iostream>
#include <list>

using namespace std;

class BreadthFirstSearch{
    int numVertices;
    list<int>* adjLists;
    bool* visited;

    public:
    BreadthFirstSearch(int vertices);
    void addEdge(int src, int dest);
    void BFS(int startVertex);
};

//Create Graph with different vertices,
// and maintain an adjacency list
BreadthFirstSearch::BreadthFirstSearch(int vertices){
    numVertices = vertices;
    adjLists = new list<int>[vertices];
}

// Add Edges to the graph
void BreadthFirstSearch::BFS(int startVertex){
    visited = new bool[numVertices];
    for(int i = 0; i < numVertices; i++){
        visited[i] = false;
    }

    list<int> queue;

    visited[startVertex] = true;
    queue.push_back(startVertex);

    list<int>::iterator i;

    while(!queue.empty()){
        int currVertex = queue.front();
        cout << "Visited " << currVertex << " ";
        queue.pop_back();

        for(i = adjLists[currVertex].begin(); i != adjLists[currVertex].end(); ++i){
            int adjVertex = *i;
            if (!visited[adjVertex]){
                visited[adjVertex] = true;
                queue.push_back(adjVertex);
            }
        }
    }
}