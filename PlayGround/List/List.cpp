#include <iostream>
#include <string>
#include <list>
#include <cstring>

using namespace std;

void printList(list<char> const &list){
    for (auto const &i: list){
        std::cout << i ;
    }

    std::cout << std::endl;
}

string convertToString(list<char> a, int size)
{
    int i;
    string s = "";
    for (i = 0; i < size; i++) {
        s = s + a.at(i);
    }
    return s;
}




int main(){
    // make string "Hello World" and string "1122334455"
    string str1 = "Hello World";
    string int1 = "1122334455";

    // turn string into list
    std::list<char> listStr1(str1.begin(), str1.end());
    std::list<char> listInt1(int1.begin(), int1.end());

    std::cout << "List of Str" << std::endl;
    printList(listStr1);

    std::cout << "List of int" << std::endl;
    printList(listInt1);
    
    // turn list string into list int
    
    std::list<int> intList;
    
    for (char c: int1) {
        intList.push_back(c-48);
    }
    for(const auto& elem: intList){
        std::cout << elem << " ";
    }
    
    std::cout << std::endl;

    // turn list into string
    string s = convertToString(listStr1, listStr1.size());


    // std::cout << std::endl << str1.size();


    // remove duplicate

    // check if 'space' inside list

    // check index space


    // remove space in list

    // swap list

    // make another list


    // merge 2 list with same type


    // cut list into 2 left and right

    // make hash map

    // check if n in keys

    // get hash_map get value of k

    // check if n in values


    // itterate hashmap
    return 0;
}
