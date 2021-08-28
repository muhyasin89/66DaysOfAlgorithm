<?php

$my_array = array(2, 4, 3, 5, 1);

list($a, $b, $c, $d, $f) = $my_array;

echo "$a $b $c $d $e $f\n";

function printList($arr)
{
    foreach ($arr as $item) {
        echo $item . " ";
    }
    echo "\n";
}


function swap($start, $end, $arr)
{
    $temp = $arr[$start];
    $arr[$start] = $arr[$end];
    $arr[$end] = $temp;

    return $arr;
}

$arr = swap(0, 1, $my_array);

printList($arr);
echo array_search(1, $my_array) . "\n";


$string_a = "IniStringPertama";
$arr_a = str_split($string_a);

printList($arr_a);
echo implode("", $arr_a) . "\n";

function printHashMap($hash)
{
    foreach ($hash as $item) {
        echo $item . " - ";
    }
}

function printYield($my_array)
{
    yield $my_array;
}

$myhashmap = array(1 => 'first', 2 => 'second', 3 => 'third');

printHashMap($myhashmap);
print_r(array_keys($myhashmap));
print_r($my_array);
printYield($my_array);

echo "============separator================\n";
print_r(array_key_exists("1", $myhashmap) . "\n");

echo (in_array('first', $myhashmap) . "\n");

$list_str = "Hello World";
$arr_str = explode(" ", $list_str);
var_dump($arr_str);

print_r(str_split($arr_str[0]));


$palind = str_split("aabcbaa");
$len = count($palind);

$left = array_slice($palind, 0, floor($len / 2));
$right = array_slice($palind, floor($len / 2));

if (count($left) != count($right)) {
    array_shift($right);
}
var_dump($left);
var_dump($right);
