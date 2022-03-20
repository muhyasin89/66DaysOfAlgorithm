#include <iostream>
#include <stdio.h>

using namespace std;

int area(int length, int breath){
    return length * breath;
}

int parameter(int length, int breath){
    int p;
    p = 2*(length+breath);

    return p;
}

int main(){
    int length = 0, breath=0;

    printf("Enter Length and Breath\n");
    std::cout << "length: ";
    std::cin  >> length;

    std::cout << endl << "Breath:" ;
    std::cin >> breath;

    int area =  length * breath;
    int peri = 2* (length+breath);

    printf("Area %d \n perimiter %d \n", area, peri);

    return 0;
}