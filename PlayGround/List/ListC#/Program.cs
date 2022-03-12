// See https://aka.ms/new-console-template for more information

static IList<T> Swap<T>(IList<T> list, int indexA, int indexB)
{
    T tmp = list[indexA];
    list[indexA] = list[indexB];
    list[indexB] = tmp;
    
    return list;
}

// make string "Hello World" and string "1122334455"
string str1, int1;
str1 = "Hello World";
int1 = "1122334455";


// turn string into list
List<char> listStr = new List<char>();
List<char> listInt = new List<char>();

listStr.AddRange(str1);
listInt.AddRange(int1);
listStr.ForEach(Console.Write);
Console.WriteLine();
listInt.ForEach(Console.Write);
Console.WriteLine();

Type listIntType = listInt.GetType().GetGenericArguments().Single();
Console.WriteLine("Type : "+listIntType);

List<int> Convert(List<char> listChar){
    List<int> intList = new List<int>();

    for(int i=0; i < listChar.Count;  i++){
        intList.Add(int.Parse(listChar[i].ToString()));
    }

    return intList;
}

List<int> arrInt = Convert(listInt);
Console.WriteLine("Type : "+arrInt.GetType());

// turn list into string
Console.WriteLine(string.Join( "", str1.ToArray()));

// check if 'space' inside list
Console.WriteLine(listStr.Any(Char.IsWhiteSpace));

// check index space
int indexSpace = listStr.FindIndex(Char.IsWhiteSpace);
Console.WriteLine(indexSpace);

// remove space in list
listStr.RemoveAt(indexSpace);
Console.WriteLine(string.Join( "", listStr.ToArray()));

// swap list
Swap(listStr, 5,6);
Console.WriteLine(string.Join( "", listStr.ToArray()));

// make another list

// remove duplicate


// merge 2 list with same type


// cut list into 2 left and right

// make hash map

// check if n in keys

// get hash_map get value of k

// check if n in values


// itterate hashmap
