// See https://aka.ms/new-console-template for more information


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

// check index space


// remove space in list

// swap list

// make another list

// remove duplicate


// merge 2 list with same type


// cut list into 2 left and right

// make hash map

// check if n in keys

// get hash_map get value of k

// check if n in values


// itterate hashmap
