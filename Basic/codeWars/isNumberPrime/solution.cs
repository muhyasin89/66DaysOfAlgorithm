public static class Kata
{
  public static bool IsPrime(int n)
  {
    // TODO
    if(n<=1){
      return false;
    }
    
    for(int i=2; i< System.Math.Sqrt(n); i++){
      if(n%i == 0){
        return false;
      }
    }
    
    return true;
  }
}