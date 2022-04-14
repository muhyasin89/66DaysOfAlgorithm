#include <cmath>

int digital_root(int n)
{
  if(n< 10){
    return n;
  }else{
    int result=0;
    
    while(n>0){
      result += (n%10);
      n = floor(n/10);
    }
    
    return digital_root(result);
  }
}