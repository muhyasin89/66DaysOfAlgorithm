#include <iostream>

using namespace std;

void swap(int *x, int *y){
    int temp;
    temp = *x;
    *x=*y;
    *y=temp;
}


int main(){
    int num1 = 10, num2=15;

    std::cout << "First Number:" << num1 << endl;
    std::cout << "Second Number:" << num2 << endl;

    return 0;
}