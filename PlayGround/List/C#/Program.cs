// See https://aka.ms/new-console-template for more information

static IList<T> Swap<T>(IList<T> list, int indexA, int indexB){
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

// turn list string to list int
Type ListIntType = listInt.GetType().GetGenericArguments().Single();
Console.WriteLine("Type :" + ListIntType);

List<int> Convert(List<char> listChar){
    List<int> intList = new List<int>();

    for(int i=0; i <listChar.Count; i++){
        intList.Add(int.Parse(listChar[i].ToString()));
    }

    return intList;
}

List<int> arrInt = Convert(listInt);
Console.WriteLine("Type :" + arrInt.GetType());

// turn list into string
Console.WriteLine(string.Join("", str1.ToArray()));

// check if 'space' inside list
Console.WriteLine(listStr.Any(char.IsWhiteSpace));

// check index space
int indexSpace = listStr.FindIndex(char.IsWhiteSpace);
Console.WriteLine(indexSpace);

// remove space in list
listStr.RemoveAt(indexSpace);
Console.WriteLine(string.Join("", listStr.ToArray()));

// swap list
Swap(listStr, 5,6);
Console.WriteLine(string.Join("", listStr.ToArray()));

// make another list 678910
List<int> arrInt2 = new List<int>();
arrInt2.Add(6);
arrInt2.Add(7);
arrInt2.Add(8);
arrInt2.Add(9);
arrInt2.Add(10);

// merge 2 list with same type
var combineArr = arrInt.Concat(arrInt2).ToList();
Console.WriteLine(string.Join("", combineArr.ToArray()));

// remove duplicate
combineArr = combineArr.Distinct().ToList();
Console.WriteLine(string.Join("", combineArr.ToArray()));

// cut list into 2 left and right
static List<List<char>> SplitList(List<char> listStr, int size){
    var list = new List<List<char>>();

    for(int i=0; i <listStr.Count; i+=size){
        list.Add(listStr.GetRange(i, Math.Min(size, listStr.Count - i)));
    }

    return list;
}

List<List<char>> result = SplitList(listStr, (listStr.Count/2));

foreach(List<char> list in result){
    Console.WriteLine("***********************");

    foreach(char item in list){
        Console.Write(item);
    }

    Console.WriteLine();
}

// make hash map
IDictionary<int, string> hash_map = new Dictionary<int, string>();
hash_map.Add(1, "first");
hash_map.Add(2, "second");
hash_map.Add(3, "third");

// check if n in keys
if(hash_map.ContainsKey(1)){
    Console.WriteLine("Hash Map contains Key");
}else{
    Console.WriteLine("Hash Map not cointains key");
}

// get hash_map get value of k
Console.WriteLine(hash_map[2]);

// itterate hashmap and find value inside hash_map
bool ValueFound = false;
foreach(KeyValuePair<int,string> kvp in hash_map){
    if(kvp.Value == "third"){
        ValueFound =true;
    }
    Console.WriteLine("Key: {0}, Value: {1}", kvp.Key, kvp.Value);
}

if(ValueFound){
    Console.WriteLine("Hash map contains Value: {0}", "third");
}else{
    Console.WriteLine("Hash map not contains Value: {0}", "third");
}
