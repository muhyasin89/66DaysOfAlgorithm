#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <cstring>

#include <bits/stdc++.h>

using namespace std;

void printList(list<char> const &list){
    for (auto const &i: list){
        std::cout << i ;
    }

    std::cout << std::endl;
}

void printCharArray(char *arr, int arrSize){
    for(int i=0; i< arrSize; i++){
        std::cout << arr[i];
    }

    std::cout << endl;
}

string convertToString(list<char> a, int size)
{
   int i;
    string s = "";

    list<char>::iterator it = a.begin();
    for (i = 0; i < size; i++) {
        s = s + *it;
        ++it;
    }
    return s;
}

void changeListToArray(list<int> intList, int* arr){
    int k = 0;
    for (int const &i: intList) {
        arr[k++] = i;
    }
}

void changeListStrToArray(list<char> listStr, char* arr){
    int k = 0;
    for (int const &i: listStr) {
        arr[k++] = i;
    }
}

void removeDuplicates(int *arr, int n, int *result)
{

	int i;

	// Initialise a set
	// to store the array values
	set<int> s;

	// Insert the array elements
	// into the set
	for (i = 0; i < n; i++) {

		// insert into set
		s.insert(arr[i]);
	}

	set<int>::iterator it;

	// Print the array with duplicates removed
	cout << "\nAfter removing duplicates:\n";
    int k =0; 
    std::cout << "endl: ";
	for (it = s.begin(); it != s.end(); ++it){
        std::cout  << " "<< k << ":" << *it << " ";
        result[k++] = *it;
    }
	cout << '\n';
}


void combineArr(int *arr1, int *arr2, int *arr3, int arr1Size, int arr2Size, int combineSize){
    for (int i = 0; i < combineSize; i++)
    {
        if (i < arr1Size) {
            arr3[i] = arr1[i];
        }
        else {
            arr3[i] = arr2[i - arr1Size];
        }
    }
 
    for (int i = 0; i < combineSize; i++) {
        std::cout << arr3[i] << ' ';
    }
}

void checkSpace(list<char> const &list){
    bool hasSpace = false;
    for (auto const &i: list){
        if(i == ' '){
            hasSpace = true;
        }
    }

    if(hasSpace){
        std::cout << "There are some Space";
    }else{
        std::cout << "There is no Space";
    }

    std::cout << std::endl;
}

int getposition(const char *array, size_t size, char c)
{
     const char* end = array + size;
     const char* match = std::find(array, end, c);
     return (end == match)? -1 : (match-array);
}

// This function removes an element x from arr[] and
// returns new size after removal (size is reduced only
// when x is present in arr[]
int deleteElement(char *arr, int n, char x)
{
    // Search x in array
    int i;
    for (i=0; i<n; i++)
        if (arr[i] == x)
            break;

    // If x found in array
    if (i < n)
    {
        // reduce size of array and move all
        // elements on space ahead
        n = n - 1;
        for (int j=i; j<n; j++)
            arr[j] = arr[j+1];
    }

    return n;
}

void printVectorChar(vector<char> newChar){
    for (int i = 0; i < newChar.size(); i++) {
      std::cout << newChar[i];
    }

    std::cout << endl;
}

void searcHashValue(unordered_map<int, string> hash_map ,string searchvalue)
{
     for (auto x : hash_map){
         if( x.second == searchvalue){
             cout<<"value present at " << x.first << " the value is:"<< x.second <<endl;
             return;
         }
     }
     cout<<"value do not exist"<<endl;
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


    // turn list char into string
    string str = convertToString(listStr1, listStr1.size());
    std::cout << str << endl;


    // turn list<int> into int[]
    int arr[intList.size()];
    std::cout << "Size of int List:" << intList.size() << endl;
    changeListToArray(intList, arr);

    for(int i=0; i < intList.size(); i++){
        std::cout << arr[i] << " " ;
    }

    // remove duplicate
    int arr1[5];
    removeDuplicates(arr, intList.size(), arr1);

    int arr1Size = sizeof(arr1)/sizeof(arr1[0]);
    std::cout << arr1Size << endl;

    for(int i=0; i < arr1Size; i++){
        std::cout << arr1[i] << " " ;
    }

    std::cout << endl;

    // check if 'space' inside list
    checkSpace(listStr1);

    // check index space
    char arrStr[listStr1.size()];
    std::cout << endl << "List size:" << listStr1.size() << endl;

    //change List<str> into char[]
    changeListStrToArray(listStr1, arrStr); 

    int arrStrSize = sizeof(arr)/ sizeof(arr[0]);
    printCharArray(arrStr, arrStrSize);

    int spaceIndex = getposition(arrStr, arrStrSize, ' ');
    std::cout << "the space is " << spaceIndex;

    // remove space in list
    arrStrSize = deleteElement(arrStr, arrStrSize, ' ');
    std::cout << endl << "Array Str Size:" << arrStrSize << endl;
	cout << endl << "Modified array is \n";
	for (int i=0; i<=arrStrSize+1; i++)
	    std::cout << arrStr[i] << " ";

    std::cout << endl;

    // make another list
    int arr2[5] = {6, 7, 8, 9, 10};
    int arr2Size = sizeof(arr2)/sizeof(arr2[0]);

    // merge 2 list with same type
    int combineSize = arr1Size + arr2Size;
    int arr3[combineSize];

    std::cout << endl <<"combine length:" << combineSize << endl;
    combineArr(arr1, arr2, arr3, arr1Size, arr2Size, combineSize);

    // swap list
    swap(arrStr[4], arrStr[5]);
    for (int i=0; i<=arrStrSize; i++)
	    std::cout << arrStr[i] << " ";

    std::cout << endl;
    
    //change array to vector
    vector<char> helloChars;

    for(int i=0; i < arrStrSize; i++){
        helloChars.push_back(arrStr[i]);
    }

    size_t half = helloChars.size() / 2;
    // cut list into 2 left and right
    if(half > 0){
        std::vector<char> firstPart(helloChars.begin(),helloChars.begin() + half);
        std::vector<char> lastPart(helloChars.begin() + half,helloChars.end());

        printVectorChar(helloChars);
        printVectorChar(firstPart);
        printVectorChar(lastPart);
    }

    // make hash map
    unordered_map<int, string> hash_map;
    hash_map[1] = "first";
    hash_map[2] = "second";
    hash_map[3] = "third";

    int k = 1;

    // check if n in keys
    if (hash_map.find(k) != hash_map.end()) {
        std::cout << k <<" Key found";
    }

    std::cout << endl;

    // get hash_map get value of k
    std::cout << "The value of K: "<< hash_map[k] << endl; 

    // check if n in values
    searcHashValue(hash_map, "second");

    std::cout << endl;

    // itterate hashmap
    for (auto x : hash_map)
      cout << x.first << " " << x.second << endl;

    return 0;
}
