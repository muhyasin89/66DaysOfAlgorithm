#include <iostream>

using namespace std;

int main(){

    int a = 10;
    int &r = a;

    std::cout << a << " and this is r " << r << endl;
    a = 25;

    std::cout << a << " and this is r " << r << endl;
    int b =30;
    r=b;

    std::cout << a << " and this is r " << r << endl;
    return 0;
}