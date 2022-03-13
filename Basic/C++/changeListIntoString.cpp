#include <iostream>

string convertListToChar(list<char> const &list){
    std::string s = "";

    for (auto const &i: list){
        s = s + i ;
    }

    return s;
}

int main(){
    std::string str1 = "Hello World";

    std::list<char> listStr(str1.begin(), str1.end());
    std::string a = convertListToChar(listStr);

    std::cout << a << std::endl;

    return 0;
}