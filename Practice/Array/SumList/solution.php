<?php


$arr = array(1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5);
$map = array();

function sumList($arr, $map)
{
    foreach ($arr as $item) {
        if (array_key_exists($item, $map)) {
            $map[$item] += 1;
        } else {
            $map[$item] = 1;
        }
    }

    return $map;
}

function printHashMap($map)
{
    foreach ($map as $key => $val) {
        echo "number: " . $key . " = " . $val . " times\n";
    }
}


$map = sumList($arr, $map);
printHashMap($map);
