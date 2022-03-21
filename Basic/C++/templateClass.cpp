#include <iostream>

using namespace std;

template<class T>
class Aritmatic{
    private:
        T a;
        T b;
    public:
        Aritmatic(T a, T b);
        T add();
        T sub();
};

template<class T>
Aritmatic<T>::Aritmatic(T a, T b){
    this->a = a;
    this->b = b;
}

template<class T>
T Aritmatic<T>::add(){
    return a + b;
}


template<class T>
T Aritmatic<T>::sub(){
    return a -b;
}


int main(){

    Aritmatic<int> ar(10, 5), ar2(15, 7);

    std::cout << "Add:" << ar.add() << endl << "Sub:" << ar.sub() << endl;
    std::cout << "Add:" << ar2.add() << endl << "Sub:" << ar2.sub() << endl;

    return 0;
}