using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;

public static class Kata
{
  public static List<string> Anagrams(string word, List<string> words)
  {
    var orderedWord = word.OrderBy(l => l).ToList();
    return words.Where(el => el.OrderBy(l => l).SequenceEqual(orderedWord)).ToList();
  }
}