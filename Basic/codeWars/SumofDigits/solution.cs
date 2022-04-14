using System;

public class Number
{
  public int DigitalRoot(long n)
  {
    
    // Your awesome code here!
    if(Convert.ToInt32(n) < 10){
      return Convert.ToInt32(n);
    }else{
      int result=0;
    
      while(Convert.ToInt32(n)>0){
        result += (Convert.ToInt32(n)%10);
        n = Convert.ToInt64(System.Math.Floor(Convert.ToDouble(Convert.ToInt32(n)/10)));
      }

      return DigitalRoot(result);
    }
  }
}