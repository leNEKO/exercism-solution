<?php

function pig_word($matches){
    $word = $matches[0];
    $alpha = implode("",range("a","z"));
    $voyelle = "aeiouy";
    $consonne = preg_replace("/[$voyelle]/","",$alpha);

    preg_match(
        "/^(squ|qu|y|[$consonne]+)([$voyelle].*)$/",
        $word,
        $matches
    );

    if(
        $matches
        && !preg_match("/ay$/",$word)
    ){
        return $matches[2].$matches[1]."ay";
    }else{
        return $word . "ay";
    }
}

function translate(string $words){
    return preg_replace_callback("/(\w+)/","pig_word", $words);
}
