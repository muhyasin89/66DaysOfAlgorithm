#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

struct Rectangle{
    int length;
    int breath;
};

int main(){
    // struct Rectangle r = {10, 5};

    // std::cout << "length: "<< r.length << " breath :" << r.breath << std::endl;

    // Rectangle *p = &r;

    struct Rectangle *p;
    //p = (struct  Rectangle *)malloc(sizeof(struct Rectangle)); // C executed

    p = new Rectangle; //  C++ code

    p -> length = 15;
    p -> breath = 7;

    std::cout << p -> length << std::endl;
    std::cout << p -> breath << std::endl;
    return 0;
}