<?php

function wordCount(string $str)
{
    preg_match_all("/\w+/u", mb_strtolower($str), $matches);
    return array_count_values($matches[0]);
}
