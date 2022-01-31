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
// cut list into 2 left and right

// make hash map

// check if n in keys

// get hash_map get value of k

// check if n in values

// itterate hashmap
}
