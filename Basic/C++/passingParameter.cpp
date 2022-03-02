#include <iostream>

using namespace std;

int add(int a, int b){
    a++;
    std::cout << a << endl;
    return 0;
}

int main(){
    int num1=10, num2=15, sum;

    sum = add(num1, num2);
    std::cout << num1 << endl;
    return 0;
}