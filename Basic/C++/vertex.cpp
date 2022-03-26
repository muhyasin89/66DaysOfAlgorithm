#include <iostream>
#include <string>

using namespace std;

struct Vertex{
    float x, y, z;
}

std::ostream& operator<<(std::ostream& stream, const Vertex& vertex){
    stream << vertex.x << ", " << vertex.y << ", "<< vertex.z;
}

int main(){
    std::vector<Vertex> vertices;

    vertices.push_back({1, 2, 3});
    vertices.push_back({4, 5, 6});

    for(int i=0; i < vertices.size(); i++){
        std::cout << vertices[i] << endl;
    }

    for(Vertex a : vertices){
        // std::cout << a << endl;
    }

    std::cin.get();
}