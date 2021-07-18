#include <iostream>
#include <cstdio>
using namespace std;

using std::endl;
using std::cin;
using std::cout;
using std::fixed;

int main() {
    // Complete the code.

    int a; long b; char c; float d; double e;

    cin >> a >> b >> c >> d;
    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    cout.precision(3);
    cout << fixed << d << endl;
    cout.precision(9);
    cout << fixed << e << endl;
    return 0;
}

