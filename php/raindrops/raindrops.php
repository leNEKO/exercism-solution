<?php
const PRIME_TO_SOUND = [
    3 => "Pling",
    5 => "Plang",
    7 => "Plong",
];

function raindrops(int $i): string
{
    $callback = function ($prime) use ($i) {
        return $i % $prime == 0;
    };

    $sounds = array_filter(PRIME_TO_SOUND, $callback, ARRAY_FILTER_USE_KEY);
    return $sounds ? implode($sounds) : $i;
}
