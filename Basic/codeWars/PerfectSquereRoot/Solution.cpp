#include <math.h>

bool is_square(int n)
{
  // TODO
  if(n >= 0 ){
      long sr = sqrt(n);
    
      return (sr*sr == n);
  }
  
  return false;
}

// reference https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/cpp