<?php
function calculate(string $q){
    // 1. Patterns
    $num = "(-?\d+)";
    $pats = [
        "/^What is $num/" => "_$1",
        "/plus $num/" => "+_$1",
        "/minus $num/" => "-_$1",
        "/multiplied by $num/" => "*_$1",
        "/divided by $num/" => "/_$1",
        "/raised to the $num\w+ power/" => "**_$1",
        "/\?$/" => "",
    ];

    // 2. Normalize
    $norm = preg_replace(array_keys($pats), array_values($pats), $q);
    $queue = explode(" ",$norm);
    $total = 0;

    // 3. ???
    foreach($queue as $do){
        $els = explode("_", $do);
        if(count($els) <= 1){
            throw new InvalidArgumentException("");
        }
        list($operator,$val) = explode("_", $do);

        switch($operator){
            case "":
            case "+":
                $total += $val;
                break;
            case "-":
                $total -= $val;
                break;
            case "*":
                $total *= $val;
                break;
            case "/":
                $total /= $val;
                break;
            case "**":
                $total **= $val;
                break;
        }
    }

    // 4. PROFIT !
    return $total;
}
