#include <iostream>

using namespace std;

int add(int a, int b){
    return  a + b;
}

int main(){
    

    int  num1 = 10, num2=15;
    std::cout << add(num1, num2);
    return 0;
}