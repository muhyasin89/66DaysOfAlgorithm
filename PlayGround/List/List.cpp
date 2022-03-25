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
    string s = convertToString(listStr1, listStr1.size());
    std::cout << s << endl;


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

    // check if 'space' inside list

    // check index space


    // remove space in list

    // swap list

    // make another list
    int arr2[5] = {6, 7, 8, 9, 10};
    int arr2Size = sizeof(arr2)/sizeof(arr2[0]);

    
    // merge 2 list with same type
    int combineSize = arr1Size + arr2Size;
    int arr3[combineSize];

    std::cout << endl <<"combine length:" << combineSize << endl;

    combineArr(arr1, arr2, arr3, arr1Size, arr2Size, combineSize);

    // cut list into 2 left and right

    // make hash map

    // check if n in keys

    // get hash_map get value of k

    // check if n in values


    // itterate hashmap
    return 0;
}
