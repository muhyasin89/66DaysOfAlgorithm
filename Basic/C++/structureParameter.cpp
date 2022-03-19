#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

struct Rectangle
{
    int length;
    int breadth;
};

// example 1
// void fun(struct Rectangle r){
//     r.length = 20;
//     cout << "Length: " << r.length << endl << "Breath:" << r.breadth << endl;
// }

struct Rectangle *fun(){
    struct Rectangle *p;

    p = new Rectangle;

    p->length=15;
    p->breadth=7;

    return p;
}

int main()
{
    // example 2
    // struct Rectangle r={10, 5};
    // fun(r);

    // printf("Length %d \n Breath %d \n", r.length, r.breadth);

    struct Rectangle *ptr = fun();

    std::cout << "Length:" << ptr->length << endl << "Breath: " << ptr->breadth << endl;
    return 0;
}