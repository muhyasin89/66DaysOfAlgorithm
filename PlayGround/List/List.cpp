#include <string>
#include <list>
#include <iostream>
#include <vector>
#include <cstring>

#include <bits/stdc++.h>

using namespace std;

void printList(list<char> list){
    for(auto const &item: list){
        std::cout << item;
    }

    std::cout << endl;
}

string convertToString(list<char> a, int size){
    string result = "";

    list<char>::iterator it = a.begin();
    for(int i=0; i< size;i++){
        result = result + *it;
        ++it;
    }

    return result;
}

void changeListToArray(list<int> intList,int *arr){
    int k = 0;
    for(int const &item: intList){
        arr[k++] = item;
    }
}

void removeDuplication(int *arr, int size, int *arr1){
    int i;
    set<int> s;

    for(i=0; i< size; i++){
        s.insert(arr[i]);
    }

    set<int>::iterator it;

    int k =0;
    for(it=s.begin(); it != s.end(); ++it){
        std::cout << " " << k << ":" << *it << " ";
        arr1[k++] = *it;
    }
    
    std::cout << endl;
}

bool checkSpace(list<char> a){
    bool hasSpace = false;
    for(auto const &c: a){
        if(c == ' '){
            hasSpace = true;
        }
    }

    return hasSpace;
}

void changeListStrToArray(list<char> chr, char *arr){
    int k=0;
    for(int const &item: chr){
        arr[k++] = item;
    }
}


void printCharArray(char *arr, int arrSize){
    for(int i=0; i< arrSize; i++){
        std::cout << arr[i];
    }

    std::cout << endl;
}

int getPosition(const char *arr, size_t size, char space){
    const char* end = arr + size;
    const char* match = std::find(arr, end, space);
    return (end == match) ? -1 : (match-arr);
}

int deleteElement(char *arr, int size, char space){
    int i;
    for(i=0;i<size;i++){
        if(arr[i] == space){
            break;
        }
    }

    if(i<size){
        size = size -1;
        for(int j=i; j<size; j++){
            arr[j] = arr[j+1];
        }
    }

    return size;
}

void combinationArr(int *arr1, int *arr2, int *arr3, int arr1Size, int arr2Size, int arr3Size){
    for(int i=0; i<arr3Size; i++){
        if(i < arr1Size){
            arr3[i] = arr1[i];
        }else{
            arr3[i] = arr2[i-arr1Size];
        }
    }

    for(int i=0; i< arr3Size; i++){
        std::cout << arr3[i] << " ";
    }

    std::cout << endl;
}

void printVectorChar(vector<char> newChars){
    for(int i=0; i<newChars.size(); i++){
        std::cout << newChars[i] << " ";
    }

    std::cout << endl;
}

void searchHashValue(unordered_map<int, string> hash_map, string searchValue){
    for(auto  x: hash_map){
        if(x.second == searchValue){
            std::cout << "Value is present at " << x.first << "The Value is "<< x.second << endl;
            return;
        }
    }

    std::cout << "Value is not exist "<< endl;
}

int main(){
    // make string "Hello World" and string "1122334455"
    string str1 = "Hello World";
    string int1 = "1122334455";

    // turn string into list
    std::list<char> listStr1(str1.begin(), str1.end());
    std::list<char> listInt1(int1.begin(), int1.end());

    std::cout << "List of Str: " << endl;
    printList(listStr1);

    std::cout << "List of Int: " << endl;
    printList(listInt1);

    // turn list string into list int
    std::list<int> intList;

    for(char c:int1){
        intList.push_back(c-48);
    }

    for(const auto& elem: intList){
        std::cout << elem << " ";
    }

    std::cout << endl;

    // turn list char into string
    string str = convertToString(listStr1, listStr1.size());
    std::cout << str << endl;
    
    // turn list<int> into int[]
    int arr[intList.size()];
    changeListToArray(intList, arr);
    
    for(int i=0; i<intList.size(); i++){
        std::cout << arr[i] << " ";
    }

    std::cout << endl;

    // remove duplicate
    int arr1[5];

    removeDuplication(arr, intList.size(), arr1);

    int arr1Size = sizeof(arr1)/ sizeof(arr1[0]);
    std::cout << "size of arr1" << arr1Size << endl;

    for(int i=0; i< arr1Size; i++){
        std::cout << arr1[i] << " ";
    }

    std::cout << endl;

    // check if 'space' inside list
    bool hasSpace = checkSpace(listStr1);
    std::cout << "Space Exist?" << hasSpace << endl;

    // change List<str> into char[]
    char arrStr[listStr1.size()];
    changeListStrToArray(listStr1, arrStr);

    int arrStrSize = sizeof(arrStr)/ sizeof(arrStr[0]);

    printCharArray(arrStr, arrStrSize);

    // check index space
    int spaceIndex = getPosition(arrStr, arrStrSize, ' ');
    std::cout << "Index of Space in Array:" << spaceIndex;

    // remove space in array
    arrStrSize = deleteElement(arrStr, arrStrSize, ' ');

    std::cout << "Modified Array is " << endl;
    for(int i=0; i< arrStrSize; i++){
        std::cout << arrStr[i] << " ";
    }

    std::cout << endl;

    // merge 2 list with same type 678910
    int arr2[5] = {6,7,8,9,10};
    int arr2Size = sizeof(arr2)/ sizeof(arr2[0]);

    int arr3[arr1Size+arr2Size];
    combinationArr(arr1, arr2, arr3, arr1Size, arr2Size, arr1Size+arr2Size);

    // swap list
    swap(arrStr[4], arrStr[5]);

    for(int i=0; i< arrStrSize; i++){
        std::cout << arrStr[i] << " ";
    }

    std::cout << endl;
    
   // change array to vector
    vector<char> helloChars;

    for(int i=0; i<arrStrSize; i++){
        helloChars.push_back(arrStr[i]);
    }
    
    // cut list into 2 left and right [Hello] [world]
    size_t half = helloChars.size()/2;

    if(half>0){
        std::vector<char> firstPart(helloChars.begin(), helloChars.begin()+ half);
        std::vector<char> lastPart(helloChars.begin()+ half, helloChars.end());

        printVectorChar(helloChars);
        printVectorChar(firstPart);
        printVectorChar(lastPart);
    }
    

    // make hash map
    unordered_map<int, string> hash_map;
    hash_map[1] = "first";
    hash_map[2] = "second";
    hash_map[3] = "third";

    // check if n in keys
    int k=1;
    if(hash_map.find(k) != hash_map.end()){
        std::cout << k << " Key Found";
    }else{
        std::cout << "Key Not Found";
    }

    std::cout << endl;

    // get hash_map get value of k
    std::cout  << "The value of K is " << hash_map[k] << endl;

    // check if n in values
    searchHashValue(hash_map, "second");

    std::cout << endl;
   

    // itterate hashmap
    for(auto x: hash_map){
        std::cout << x.first << ":" << x.second << endl;
    }

    return 0;
}
