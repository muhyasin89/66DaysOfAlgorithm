// See https://aka.ms/new-console-template for more information

static IList<T> Swap<T>(IList<T> l, int indexA, int indexB){
    T tmp =l[indexA];
    l[indexA] = l[indexB];
    l[indexB] = tmp;

    return l;
}

// make string "Hello World" and string "1122334455"
string str1, int1;
str1 = "Hello World";
int1 =  "1122334455";

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
Console.WriteLine("Type :"+ ListIntType);

List<int> Convert(List<char> listChar){
    List<int> intList = new List<int>();

    for(int i=0;i< listChar.Count; i++){
        intList.Add(int.Parse(listChar[i].ToString()));
    }

    return intList;
}

List<int> arrInt = Convert(listInt);
Console.WriteLine("Type :"+arrInt.GetType());

// turn list into string
Console.WriteLine(string.Join("", str1.ToArray()));

// check if 'space' inside list
Console.WriteLine(listStr.Any(char.IsWhiteSpace));

// check index space
int indexSpace = listStr.FindIndex(char.IsWhiteSpace);
Console.WriteLine("Index Of Space:" + indexSpace);

// remove space in list
listStr.RemoveAt(indexSpace);
Console.WriteLine(string.Join("", listStr.ToArray()));

// swap list
Swap(listStr, 5, 6);
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
    var l = new List<List<char>>();

    for(int i=0; i< listStr.Count; i+=size){
        l.Add(listStr.GetRange(i, Math.Min(size, listStr.Count -i)));
    }

    return l;
}

List<List<char>> result = SplitList(listStr, (listStr.Count/2));

foreach(List<char> l in result){
    Console.WriteLine("***********************");

    foreach(char item in l){
        Console.Write(item);
    }

    Console.WriteLine();
}
// make hash map
IDictionary<int, string> hash_map = new Dictionary<int, string>();
hash_map.Add(1, "first");
hash_map.Add(2, "second");
hash_map.Add(3, "third");

// get hash_map get value of k
int k =1;
if(hash_map.ContainsKey(k)){
    Console.WriteLine("Hash map has contain key" +k);
}else{
    Console.WriteLine("Hash Map not found key:"+ k);
}

// itterate hashmap and find value inside hash_map
bool hasValue = false;
string ValueCheck = "second";
foreach(KeyValuePair<int, string> item in hash_map){
    if(item.Value == ValueCheck){
        hasValue = true;
    }
    Console.WriteLine("Key {0}, Value {1}", item.Key, item.Value);
}

if(hasValue){
    Console.WriteLine("Hash Map has Value of "+ ValueCheck);
}else{
    Console.WriteLine("Hash Map has No Value of "+ValueCheck);
}
