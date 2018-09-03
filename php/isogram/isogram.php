<?php
// utf-8 VS php ... hope to learn there is a clean way of dealing with this
function split($str, $len = 1)
{
    $arr = [];
    $length = mb_strlen($str, 'UTF-8');
    for ($i = 0; $i < $length; $i += $len) {
        $arr[] = mb_substr($str, $i, $len, 'UTF-8');
    }
    return $arr;
}

function isIsogram(string $str): bool
{
    // to lower alpha only
    $normalized = preg_replace("/\W/u", "", mb_strtolower($str));

    $c = [];
    foreach (split($normalized) as $k) {
        if (in_array($k, $c)) {
            return false;
        } else {
            $c[] = $k;
        }
    }

    return true;
}
