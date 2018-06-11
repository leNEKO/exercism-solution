<?php

function abracadabra(string $str, bool $ascii_mode = true){
    $arr = preg_split( // only decent way to split UTF-8 string ?
        "//u",
        mb_strtolower(trim($str)), // case insensitive
        -1, PREG_SPLIT_NO_EMPTY
    );
    sort($arr);
    return implode("", $arr);
}

function detectAnagrams(string $word, array $candidates){
    $anagrams = [];
    $ws = abracadabra($word);
    foreach($candidates as $c){
        $cs = abracadabra($c);
        if(
            ($cs === $ws)
            && mb_strtolower($word) != mb_strtolower($c)
        ){
            $anagrams[] = $c;
        }
    }
    return $anagrams;
}