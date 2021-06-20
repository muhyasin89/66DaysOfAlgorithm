function lateRide($n) {
    return array_sum(str_split(date('Hi', mktime(0,$n))));
}
