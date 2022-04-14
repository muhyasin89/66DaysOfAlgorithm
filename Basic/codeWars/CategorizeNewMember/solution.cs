using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static IEnumerable<string> OpenOrSenior(int[][] data)
    {
       List<String> list = new List<string>();

        foreach(int[] person in data){
          if(person[0] >= 55 && person[1] > 7){
            list.Add("Senior");
          }else{
            list.Add("Open");
          }
        }
      
      String[] result = list.ToArray();
      
      return result;

    }
}