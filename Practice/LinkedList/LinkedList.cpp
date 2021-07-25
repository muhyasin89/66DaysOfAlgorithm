#include <iostream>
#include <list>
#include <iterator>

using namespace std;

class Node
{
public:
    int data;
    Node *next;
}

void
setNode(list<int> nums)
{
    Node curr = new Node();
    Node temp = new Node();
    list<int>::iterator it;
    std::vector<int>::iterator nth;
    for (it = nums.begin(); it != nums.end(); it++)
    {
        curr->data = *it;
        if (it != nums.end())
        {
            std::cout << ":" << *it;
            nth = it + 1;

            std::cout << ":" << *nth;

            // temp->data = *next_it;
            // curr->next = temp;
            // curr = temp;
        }
    }
}

//printing the element in list
void showList(list<int> nums)
{
    list<int>::iterator it;
    for (it = nums.begin(); it != nums.end(); it++)
    {
        std::cout << "->" << *it;
    }
    std::cout << '\n';
}

int main()
{
    list<int> list_1 = {2, 4, 1, 5, 3, 7, 10, 8, 9};
    showList(list_1);

    list<int> list_2 = {4, 3, 1, 10, 5, 7, 6, 8, 9};
    showList(list_2);
}