#include <iostream>
#include <fstream>
#include <cstdlib>
#include <list>
#include <ctime>

using namespace std;

void randomNumberGen(int max, int n);
void printList();

int main()
{
    int max = 20;
    int n = 10;
    list<int> number;

    srand(time(NULL));
    // list<int> number = randomNumberGen(max, n);

    // printList(list<int> number);

    return 0;
}

void randomNumberGen(int max, int n)
{
    int max_number = max;
    int rand_int;
    list<int> number;

    for (int i = 0; i < number.size(); i++)
    {
        rand_int = rand() % max_number;
        number.push_front(rand_int);
    }
}

void printList(list<int> number)
{
    list<int>::iterator it;

    for (it = number.begin(); it != number.end(); ++it)
    {
        std::cout << *it;
    }

    std::cout << std::endl;
}