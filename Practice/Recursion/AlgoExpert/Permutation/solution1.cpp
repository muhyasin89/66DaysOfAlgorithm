#include <vector>
using namespace std;
void permutationsHelper(vector<int> array, vector<int> currentPermutation, 
											vector<vector<int>> *permutations);

//upper Bound: O(n^2*n!) time| O(n*n!)space
// Roughly: O(n*n!) time | O(n*n!) space
vector<vector<int>> getPermutations(vector<int> array) {
  // Write your code here.
	vector<vector<int>> permutations;
	permutationsHelper(array, {}, &permutations);
  
	return permutations;
}

void permutationsHelper(vector<int> array, vector<int> currentPermutation, 
											vector<vector<int>> *permutations){
	if(array.size() == 0 && currentPermutation.size() > 0){
		permutations->push_back(currentPermutation);
	}else{
		for(int i=0; i< array.size(); i++){
				vector<int> newArray;
				newArray.insert(newArray.end(), array.begin(), array.begin()+i);
				newArray.insert(newArray.end(), array.begin() + i +1, array.end());

				vector<int> newPermutation = currentPermutation;
				newPermutation.push_back(array[i]);
				permutationsHelper(newArray, newPermutation, permutations);
		}
		
	}
}
