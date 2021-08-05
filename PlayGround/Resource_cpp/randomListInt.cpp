#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;

void randomNumberGen(int max, int n);

int main()
{
    int max = 20;
    int n = 10;

    srand(time(NULL));
    randomNumberGen(max, n);

    return 0;
}

void randomNumberGen(int max, int n)
{
    int max_number = max;
    int number[n];
    for (int i = 0; i < 10; i++)
    {
        number[i] = rand() % max_number;
        std::cout << number[i] << std::endl;
    }
}