using namespace std;

unordered_map<int, int> memoize;
memoize[1]=0;
memoize[2]=1;

int getNthFib(int n, unordered_map<int, int> memoize) {
	
  // Write your code here.
	if(memoize.find(n)){
		return memoize[n];
	}else{
		memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize);
		return memoize[n];
	}
}