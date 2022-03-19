#include <iostream>

using namespace std;

void fun(int *A, int n){
    //std::cout << sizeof(A)/sizeof(A[0]) << std::endl;
 
    for(int i=0; i<n; i++){
        std::cout << A[i] << " ";
    }

    std::cout << endl;

}   

int * fun1(int size){
    int *p;
    p = new int[size];

    for(int i=0; i< size; i++){
        p[i] = i+1;
    }

    return p;
}

int main(){
    int A[] = {2, 4, 6, 8, 10};
    int n=5;

    fun(A, n);

    // std::cout << sizeof(A)/sizeof(A[0]) << std::endl;

    for(int x:A){
        std::cout << x << " ";
    }

    int *ptr, sz=5;

    ptr=fun1(sz);

    for(int i=0; i< sz; i++){
        std::cout << ptr[i];
    }
    std::cout << endl;

    return 0;
}