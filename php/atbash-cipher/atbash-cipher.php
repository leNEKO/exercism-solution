<?php
//  factorized :)
function codec(string $text): string
{
    $ABC = implode("", range("a", "z")); // ascii
    $ZYX = strrev($ABC);
    $normalized = preg_replace("/\W/", "", strtolower($text));
    return strtr($normalized, $ABC, $ZYX);
}

function encode(string $text): string
{
    return trim(chunk_split(codec($text), 5, " "));
}

// ah ? there is no decode test for the php version ?
function decode(string $text): string
{
    return codec($text);
}
