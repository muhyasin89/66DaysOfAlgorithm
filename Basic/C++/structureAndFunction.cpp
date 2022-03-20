#include <iostream>
#include <stdio.h>

using namespace std;

struct Rectangle{
    int length;
    int breath;
};

void initialise(struct Rectangle *r, int l, int b){
    r -> length = l;
    r -> breath = b;
}

int area(struct Rectangle r)
{
    return r.length * r.breath;   
}

int perimeter(Rectangle r){
    int p;
    p = 2 * (r.length + r.breath);

    return p;
}

int main(){
    Rectangle r = {0, 0};

    int l, b;
    printf("Enter Length and Breath\n");

    std::cout << "Length:";
    std::cin >> l;

    std::cout << "Breath:";
    std::cin >> b;

    initialise(&r, l, b);

    int a = area(r);
    int peri = perimeter(r);

    printf("Area=%d \nPerimeter=%d \n", a, peri);


    return 0;
}