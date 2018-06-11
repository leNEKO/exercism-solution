<?php

function wordCount(string $str){
    $words = [];
    preg_match_all("/\w+/u",$str, $matches);
    foreach($matches[0] as $word){
        $lcase = mb_strtolower($word);
        if(!isset($words[$lcase])){
            $words[$lcase] = 0;
        }
        @$words[$lcase] ++;
    }
    return $words;
}
