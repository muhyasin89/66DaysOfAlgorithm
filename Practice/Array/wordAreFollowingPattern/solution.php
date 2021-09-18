<?php
$string1 = "abba";
$str1 = "dog cat cat dog";
# result True

$string2 = "abba";
$str2 = "dog cat cat fish";
# return False


function areFollowingPattern($s, $str)
{
    $list_s = str_split($s);
    $list_str = explode(" ", $str);
    $map = array();

    if (count($list_s) != count($list_str)) {
        return false;
    }

    for ($i = 0; $i < count($list_s); $i++) {
        if (array_key_exists($list_s[$i], $map)) {
            if ($map[$list_s[$i]] != $list_str[$i]) {
                return false;
            }
        } else {
            $map[$list_s[$i]] = $list_str[$i];
        }
    }

    return true;
}

echo areFollowingPattern($string1, $str1) ? "true\n" : "false\n";
echo areFollowingPattern($string2, $str2) ? "true\n" : "false\n";
