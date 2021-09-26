<?php
$str1 = "abba";
$string1 = "dog cat cat dog";
# result True

$str2 = "abba";
$string2 = "dog cat cat fish";
# return False


function areFollowingPattern($str1, $string1)
{
    $list_str = str_split($str1);
    $list_string = explode(" ", $string1);
    $hash_map = array();

    if (count($list_str) != count($list_string)) {
        return false;
    }

    for ($i = 0; $i < count($list_str); $i++) {
        $temp = $list_str[$i];

        if (array_key_exists($temp, $hash_map)) {
            if ($hash_map[$temp] != $list_string[$i]) {
                return false;
            }
        } else {
            $hash_map[$temp] = $list_string[$i];
        }
    }

    return true;
}


echo areFollowingPattern($str1, $string1) ? "true\n" : "false\n";
echo areFollowingPattern($str2, $string2) ? "true\n" : "false\n";
