#include <vector>
using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum) {
  // Write your code here.
	unordered_map<int, int> map;
	vector<int> result;
	
	for(int i=0; i< array.size(); i++){
		int numberToFind = targetSum - array[i];
		
		if(map.find(numberToFind) != map.end()){
				result.push_back(numberToFind);
				result.push_back(array[i]);
				return result;
		}else{
			map[array[i]] = i;	
		}
	}
	return result;
}
