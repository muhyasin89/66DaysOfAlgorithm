<?php

$arr = array(1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5);
$hash_map = array();

// number 1 = 3 times

function SumList($hash_map, $arr)
{
    foreach ($arr as $item) {
        if (array_key_exists($item, $hash_map)) {
            $hash_map[$item] += 1;
        } else {
            $hash_map[$item] = 1;
        }
    }
    return $hash_map;
}


function printHashMap($hash_map)
{
    foreach ($hash_map as $key => $val) {
        echo "number " . $key . " = " . $val . " times\n";
    }
}

$hash_map  = SumList($hash_map, $arr);
printHashMap($hash_map);
