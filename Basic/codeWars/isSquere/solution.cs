using System;

public class Kata
{
  public static bool IsSquare(int n)
  {
    //Your code goes here!
    if(n >= 0){
      double result = Math.Sqrt(n);
      
      return (result*result == n);
    }
    
    return false;
  }
}