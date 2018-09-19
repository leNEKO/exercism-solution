<?php

const system = [
    1000 => "M",
    900 => "CM",
    500 => "D",
    400 => "CD",
    100 => "C",
    90 => "XC",
    50 => "L",
    40 => "XL",
    10 => "X",
    9 => "IX",
    5 => "V",
    4 => "IV",
    1 => "I",
];

function toRoman(int $i)
{

    $output = "";

    foreach (system as $arab => $roman) {
        $q = intdiv($i, $arab); # quotient
        $i %= $arab; # remainder
        $output .= str_repeat($roman, $q);
    }

    return $output;
}

toRoman(10);
