#include <stdio.h>
#include <iostream>

using namespace std;

struct Rectangle{
    int length;
    int breadth;
} r1;



int main(){
    
    struct Rectangle r1={10, 5};
   
    r1.length = 15;
    r1.breadth = 7;

    std::cout << r1.length << std::endl;
    std::cout << r1.breadth << std::endl;

    return 0;
}