<?php
function isPangram(string $str): bool
{
    $lower = strtolower($str);
    preg_match_all('/[a-z]/', $lower, $m);
    $letters = array_unique($m[0]);
    sort($letters);
    return $letters === range("a", "z");
}
