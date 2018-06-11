<?php
setlocale(LC_ALL,'fr_FR.UTF-8'); // my french

function isPangram(string $str): bool{
    // normalize
    $trimmed = trim($str);

    $ascii = iconv("UTF-8", "ASCII//TRANSLIT", $trimmed); // bonus
    $lower = strtolower($ascii);

    // unique letters
    $letters = array_unique(
        str_split(
            preg_replace("/[^a-z]/", "", $lower)
        )
    );
    sort($letters);
    return $trimmed && $letters === range("a","z");
}
