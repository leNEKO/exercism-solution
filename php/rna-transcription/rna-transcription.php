<?php

function toRNA(string $seq): string{
    return strtr($seq, [
        "G" => "C",
        "C" => "G",
        "T" => "A",
        "A" => "U",
    ]);
}