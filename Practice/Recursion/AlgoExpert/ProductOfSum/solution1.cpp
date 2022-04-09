#include <any>
#include <vector>

using namespace std;

// Tip: You can use el.type() == typeid(vector<any>) to check whether an item is
// a list or an integer.
// If you know an element of the array is vector<any> you can cast it using:
//     any_cast<vector<any>>(element)
// If you know an element of the array is an int you can cast it using:
//     any_cast<int>(element)
int productSum(vector<any> array, int multiplier=1) {
  // Write your code here.
  int result=0;
  // Write your code here.
	
	for (auto e : array) {
		if (e.type() == typeid(vector<any>)){
			result += productSum(any_cast<vector<any>>(e), multiplier+1);
		}else{
			result += any_cast<int>(e);
			
		}
	}
  return result*multiplier;
}
