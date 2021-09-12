<?php
// make string "Hello World" and string "11223344"
$str1 = "Hello World";
$int1 = "11223344";


echo "Str: " . $str1 . " Int:" . $int1 . "\n";
// turn string into list
// $list_str = explode(" ", $str1);
$list_str = str_split($str1);
$list_int = str_split($int1);

print_r($list_str);
print_r($list_int);

// turn list int into list
$list_int = array_map('intval', $list_int);
print_r($list_int);

// remove duplicate
$list_int = array_unique($list_int);
print_r($list_int);

// check index space
$ind_space = array_search(" ", $list_str);
print($ind_space);

// remove space in list
unset($list_str[$ind_space]);
print_r($list_str);

// turn list into string
echo implode(" ", $list_str) . "\n";

// swap list
function swap($ind1, $ind2, $list_arr)
{
    $temp = $list_arr[$ind1];
    $list_arr[$ind1] = $list_arr[$ind2];
    $list_arr[$ind2] = $temp;

    return $list_arr;
}

swap(4, 5, $list_str);
print_r($list_str);


// make another list
$arr_int2 = array(6, 7, 8, 9, 10);

// merge 2 list with same type
$arr_int1 = array_merge($list_int, $arr_int2);
print_r($arr_int1);

// check if 'k' inside list
echo in_array(4, $arr_int1) . "\n";

// cut list into 2 left and right
$len = count($list_str);
$left = array_slice($list_str, 0, $len / 2);
$right = array_slice($list_str, $len / 2);

print_r($left);
print_r($right);

// make hash map
$fistHashMap = array(1 => 'first', 2 => 'second', 3 => 'third');

// check if n in keys
echo array_key_exists(1, $fistHashMap) . "\n";

// get value of n
echo $fistHashMap[1] . "\n";

// check if n in values
echo in_array('first', $fistHashMap) . "\n";

// itterate hash
foreach ($fistHashMap as $key => $value) {
    echo $key . " = " . $value . "\n";
}
