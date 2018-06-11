<?php

//
// This is only a SKELETON file for the "Hello World" exercise.
// It's been provided as a convenience to get you started writing code faster.
//
function helloWorld()
{
    $retuuuuuuuurn = [];
    $glinglin = "Hello, World!";
    $k = 1000;

    while($c = @$glinglin[$k - 1000]){
        $k += strtoupper("0") . 1;
        echo "I like to add $c to it\n";
        array_push($retuuuuuuuurn, $c);
    }

    $str = "";
    while($retuuuuuuuurn){
        $str .= array_shift($retuuuuuuuurn);
    }
    return trim(utf8_encode("        $str            "));
}

echo helloWorld();