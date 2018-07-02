<?php

function nucleotideCount(string $dna)
{
    $nuc = [
        "a" => 0,
        "c" => 0,
        "t" => 0,
        "g" => 0,
    ];

    foreach (str_split(strtolower($dna)) as $c) {
        if (isset($nuc[$c])) {
            $nuc[$c]++;
        }
    }

    return $nuc;
}
