<?php
$dict_map = array("{" => "}", "[" => "]", "(" => ")", "<" => ">");

$inp_str = "[]";  # expected True
$inp_str1 = "{([{}()[]])}";  # expected True
$inp_str2 = "{(][)}";  # expected False
$inp_str3 = "][";  # expected False
$inp_str4 = "{<[adadas]@1234>#$%^}";  # expected True
$inp_str5 = "{{{{{"; # expected False


function ValidBracket($str1, $dict_map)
{
    $list_bracket = array();
    $list_str = str_split($str1);

    for ($i = 0; $i < count($list_str); $i++) {
        $temp = $list_str[$i];
        if (in_array($temp, $dict_map) && $i < 0) {
            return false;
        } elseif (array_key_exists($temp, $dict_map)) {
            array_push($list_bracket, $temp);
        } elseif (in_array($temp, $dict_map)) {
            if (count($list_bracket) > 0) {
                if ($dict_map[end($list_bracket)] != $temp) {
                    return false;
                } else {
                    array_pop($list_bracket);
                }
            }
        }
    }

    if (count($list_bracket) > 0) {
        return false;
    }

    return true;
}

echo ValidBracket($inp_str, $dict_map) ? "true\n" : "false\n";
echo ValidBracket($inp_str1, $dict_map) ? "true\n" : "false\n";
echo ValidBracket($inp_str2, $dict_map) ? "true\n" : "false\n";
echo ValidBracket($inp_str3, $dict_map) ? "true\n" : "false\n";
echo ValidBracket($inp_str4, $dict_map) ? "true\n" : "false\n";
echo ValidBracket($inp_str5, $dict_map) ? "true\n" : "false\n";
