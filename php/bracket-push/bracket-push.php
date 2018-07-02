<?php

function brackets_match(string $str): bool
{
    $symbols = [
        "braces" => '{}',
        "parentheses" => '()',
        "brackets" => '[]',
    ];
    $open = [];

    foreach (str_split($str) as $c) {
        foreach ($symbols as $symbol => $pairs) {
            if ($c === $pairs[0]) {
                $open[] = $symbol;
            } elseif ($c === $pairs[1]) {
                if (array_pop($open) !== $symbol) {
                    return false;
                }
            }
        }
    }
    return empty($open);
}
