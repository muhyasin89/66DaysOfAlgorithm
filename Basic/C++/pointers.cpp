#include <stdio.h>
#include <iostream>

using namespace std;
int main(){
    int a = 10;
    int *p;
    p = &a;

    int A[5] = {1,4,5,6,7};
    int *P;
    P=A;

    for(int i=0; i<5;i++){
        std::cout << P[i];
        if(i != 4){
            std::cout << ",";
        }
    }

    std::cout << endl;

    std::cout << a << endl;
    printf("using pointer %d %d", *p, &a);

    std::cout << endl << "========way number 2 =======" << endl;

    int *x;
    x = new int[5];

    x[0] = 10;  x[1] = 5; x[2] = 14; x[3] = 21; x[4] = 31;
    for(int i = 0; i < 5; i++){
        std::cout << x[i] ;
        if(i != sizeof(x)){
            std::cout << " , ";
        }else{
            std::cout << endl;
        }
    }

    delete [ ] x;
    free(x);

    return 0;
}