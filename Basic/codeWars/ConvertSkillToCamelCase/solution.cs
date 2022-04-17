using System;

public class Kata
{
  
  public string FirstLetterToUpper(string str)
  {
      if (str == null)
          return null;

      if (str.Length > 1)
          return char.ToUpper(str[0]) + str.Substring(1);

      return str.ToUpper();
  }
  
  public static string ToCamelCase(string str)
  {
    string str1 = str.Replace("_", "-");
    
    string[] words = str1.Split("-");
    
    for(int i=0; i < words.Length ; i++){
      if(i != 0){
        words[i] = FirstLetterToUpper(words[i]);
      }
    }
    
    return string.Join("", words);
  }
}