using namespace std;

int getNthFib(int n) {
  // Write your code here.
	int lastTwo[2] = {0, 1};
	int counter = 3;
	
	while(counter <=n){
		int nextFib = lastTwo[0]+ lastTwo[1];
		lastTwo[0]=lastTwo[1];
		lastTwo[1]=nextFib;
		counter +=1;
	}
	if(n>1){
		return lastTwo[1];
	}else{
		return lastTwo[0];
	}
}