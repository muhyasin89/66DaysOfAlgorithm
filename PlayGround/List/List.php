<?php
// make string "Hello World" and string "1122334455"
$str1 = "Hello World";
$int1 = "1122334455";

echo "Str:" . $str1 . " Int:" . $int1 . "\n";

// turn string into list
$list_str = str_split($str1);
$list_int = str_split($int1);

print_r($list_str);
print_r($list_int);

// turn list string  into list int
$list_int = array_map('intval', $list_int);
print_r($list_int);

// remove duplicate
$list_int = array_unique($list_int);
print_r($list_int);

// check if 'space' inside list
echo in_array(" ", $list_str) . "\n";

// check index space
$ind_space = array_search(" ", $list_str);
echo $ind_space . "\n";

// remove space in list
unset($list_str[$ind_space]);
print_r($list_str);

// turn list into string
echo implode(" ", $list_str) . "\n";

// swap list
function swap($ind1, $ind2, $arr)
{
    $temp = $arr[$ind1];
    $arr[$ind1] = $arr[$ind2];
    $arr[$ind2] = $temp;

    return $arr;
}
$list_str = swap(4, 6, $list_str);
print_r($list_str);

// make another list
$list_int1 = array(6, 7, 8, 9, 10);

// merge 2 list with same type
$list_int = array_merge($list_int, $list_int1);
print_r($list_int);

// cut list into 2 left and right
$mid = count($list_str) / 2;
$left = array_slice($list_str, 0, $mid);
$right = array_slice($list_str, $mid);
print_r($left);
print_r($right);

// make hash map
$fistHashMap = array(1 => "first", 2 => "second", 3 => "third");

// check if n in keys
echo array_key_exists(1, $fistHashMap) . "\n";

// get value of n
echo $fistHashMap[1] . "\n";

// check if n in values
echo in_array("first", $fistHashMap) . "\n";

// itterate hash
foreach ($fistHashMap as $key => $val) {
    echo "Key: " . $key . " Val:" . $val . "\n";
}