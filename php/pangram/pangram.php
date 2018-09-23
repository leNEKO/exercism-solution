<?php
function isPangram(string $str): bool
{
    if (empty($str)) {
        return false;
    }

    preg_match_all('/[a-z]/i', $str, $m);
    $letters = array_unique($m[0]);
    return count($letters) >= 26;
}
