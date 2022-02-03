import 'dart:collection';

List<String> swap(int x, int y, list_str) {
  var tmp = list_str[x];
  list_str[x] = list_str[y];
  list_str[y] = tmp;

  return list_str;
}

void main() {
  // make string "Hello World" and string "1122334455"
  String str1 = "Hello World";
  String int1 = "1122334455";

  print(str1);
  print(int1);

// turn string into list
  List<String> list_str = str1.split("");
  print(list_str);

  List<String> list_int = int1.split("");
  print(list_int);
  print(list_int.runtimeType);

// turn list string into list int
  List<int> arr_int = list_int.map(int.parse).toList();
  print(arr_int);
  print(arr_int.runtimeType);

// turn list into string
  print(list_str.join());

// remove duplicate
  arr_int = arr_int.toSet().toList();
  print(arr_int);

// check if 'space' inside list
  print(list_str.contains(" "));

// check index space
  int index_space = list_str.indexOf(" ");
  print(index_space);

// remove space in list
  list_str.removeAt(index_space);
  print(list_str);

// swap list
  list_str = swap(5, 6, list_str);
  print(list_str);

// make another list
  List<int> arr_int2 = [6, 7, 8, 9, 10];

// merge 2 list with same type
  arr_int = arr_int + arr_int2;
  print(arr_int);

// remove duplicate number
  print(arr_int.toSet().toList());

// cut list into 2 left and right
  var list_length = (list_str.length - 1);
  var mid = (list_length / 2).floor();
  List<String> left = list_str.sublist(0, mid);
  List<String> right = list_str.sublist(mid + 1, list_length);

  print(left);
  print(right);

// make hash map
  Map<int, String> fistHashMap = {1: "first", 2: "second", 3: "third"};

// check if n in keys
  print(fistHashMap.containsKey(1));
// get hash_map get value of k
  print(fistHashMap[1]);
// check if n in values
  print(fistHashMap.containsKey("four"));
// itterate hashmap
  fistHashMap.forEach((key, value) {
    print("$key = $value");
  });
}
