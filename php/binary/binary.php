<?php
function parse_binary(string $binary): int
{
    if (preg_match("/[^01]/", $binary)) {
        throw new \InvalidArgumentException("Not a valid input (only 0 and 1 please)");
    }
    $mode = 2; // it's binary so…
    $pos = strrev($binary);
    $total = 0;
    foreach (str_split($pos) as $pow => $val) {
        $total += $val * $mode ** $pow;
    }
    return $total;
}
