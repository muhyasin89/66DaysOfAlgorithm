
#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <cstring>

#include <bits/stdc++.h>

using namespace std;

void printList(list<char> const &list){
    for(auto const &i: list){
        std::cout << i;
    }

    std::cout << endl;
}

string convertToString(list<char> a, int size){
    string s="";

    list<char>::iterator it = a.begin();
    for(int i=0; i < size; i++){
        s = s + *it;
        ++it;
    }

    return s;
}

void removeDuplicates(int *arr, int n, int *result){
    int i;
    set<int> s;

    for(i=0; i < n; i++){
        s.insert(arr[i]);
    }
    
    set<int>::iterator it;

    std::cout << endl;
    int k =0;
    for(it=s.begin(); it != s.end(); ++it){
        std::cout << " " << k << ":"<< *it << " ";
        result[k++] = *it;
    }

    std::cout << endl;
}

void changeListToArray(list<int> intList, int* arr){
    int k=0;
    for(int const &i: intList){
        arr[k++] =i;
    }
}

bool checkSpace(list<char> const &list){
    bool hasSpace = false;

    for(auto const &i: list){
        if(i == ' '){
            hasSpace=true;
        }
    }

    return hasSpace;
}

void changeListStrToArray(list<char> listStr, char* arr){
    int k=0;
    for(int const &i: listStr){
        arr[k++] = i;
    }
}

void printCharArray(char *arr, int arrSize){
    for(int i=0; i< arrSize; i++){
        std::cout << arr[i];
    }
}

int getPosition(const char *array, size_t size, char space){
    const char* end = array + size;
    const char* match = std::find(array, end, space);
    return (end == match) ? -1 : (match - array);
}

int deleteElement(char *arr, int n, char space){
    int i;
    for(i=0; i < n; i++){
        if(arr[i]== space){
            break;
        }
    }

    if(i < n){
        n = n-1;
        for(int j=i; j< n; j++){
            arr[j] = arr[j+1];
        }
    }

    return n;
}

void combinationArr(int *arr1, int *arr2, int *arr3, int arr1Size, int arr2Size, int combineSize){
    for(int i=0; i< combineSize; i++){
        if(i < arr1Size){
            arr3[i]=arr1[i];
        }else{
            arr3[i] = arr2[i-arr1Size];
        }
    }

    for(int i=0; i< combineSize; i++){
        std::cout << arr3[i] << " ";
    }

    std::cout << endl;

}

void printVectorChar(vector<char> newChar){
    for(int i=0; i < newChar.size(); i++){
        std::cout << newChar[i];
    }

    std::cout << endl;
}

void searchHashValue(unordered_map<int, string> hash_map, string searchValue){
    for(auto x: hash_map){
        if(x.second == searchValue){
            std::cout << "Value Present at "<< x.first << " the value is:" << x.second << endl;
            return;
        }
    }

    std::cout << "Value do not exist "<< endl;
}

int main(){
    // make string "Hello World" and string "1122334455"
    string str1 = "Hello World";
    string int1 = "1122334455";

    // turn string into list
    std::list<char> listStr1(str1.begin(), str1.end());
    std::list<char> listInt1(int1.begin(), int1.end());

    std::cout << "List Str" << endl;
    printList(listStr1);

    std::cout << "List Int" << endl;
    printList(listInt1);

    // turn list string into list int
    std::list<int> intList;

    for(char c: int1){
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

    std::cout << "Size of List is " << intList.size() << endl;

    changeListToArray(intList, arr);

    for(int i=0; i < intList.size(); i++){
        std::cout << arr[i] << " " ;
    }

    // remove duplicate
    int arr1[5];
    removeDuplicates(arr, intList.size(), arr1);

    int arr1Size = sizeof(arr1)/sizeof(arr1[0]);

    for(int i=0; i < arr1Size; i++){
        std::cout << arr1[i] << " ";
    }

    std::cout << endl;

    // check if 'space' inside list
    bool hasSpace = checkSpace(listStr1);

    std::cout << hasSpace << endl;
   
    //change List<str> into char[]
    char arrStr[listStr1.size()];
    std::cout << "List size:" << listStr1.size() << endl;

    changeListStrToArray(listStr1, arrStr);

    int arrStrSize = sizeof(arrStr)/ sizeof(arrStr[0]);
    printCharArray(arrStr, arrStrSize);
    std::cout << endl;

    // check space index in array
    int spaceIndex = getPosition(arrStr, arrStrSize, ' ');
    std::cout << "The Space Index is " << spaceIndex << endl;

    // remove space in list
    arrStrSize = deleteElement(arrStr, arrStrSize, ' ');
    std::cout <<"Array Size: " << arrStrSize << endl;
    std::cout << "Modified Array is \n";
    for(int i=0; i < arrStrSize; i++){
        std::cout << arrStr[i] << " ";
    }
    std::cout << endl;

    // make another list 678910
    int arr2[5] = {6,7,8,9,10};
    int arr2Size = sizeof(arr2)/ sizeof(arr2[0]);

    int arr3[arr1Size+arr2Size];
    std::cout << "Combination Size: " << arr1Size+arr2Size << endl;

    // merge 2 list with same type
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

    // check if n in keys hash_map[n]
    int k=1;
    if(hash_map.find(k) != hash_map.end()){
        std::cout << k << " Key found";
    }

    std::cout << endl;

    // get hash_map get value of k
    std::cout << "The value of K:" << hash_map[k] << endl;

    // check if n in values
    searchHashValue(hash_map, "second");

    std::cout << endl;

    // itterate hashmap
    for(auto x: hash_map){
        std::cout << x.first << " : " << x.second << endl;
    }
    return 0;
}