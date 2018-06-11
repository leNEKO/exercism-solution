<?php
function encode($input)
{
    $encoded = "";
    if($input){
        $last_char = "";
        $counter = 1;
        foreach(str_split($input) as $char){
            if($char === $last_char){
                $counter++;
            }elseif($last_char !== ""){
                if($counter > 1){
                    $encoded .= $counter;
                }
                $encoded .= $last_char;
                $counter = 1;
            }
            $last_char = $char;
        }
        if($counter > 1){
            $encoded .= $counter;
        }
        $encoded .= $last_char;
    }
    return $encoded;
}

function decode($input): string
{
    $decoded = "";
    $digit = "";

    foreach(str_split($input) as $char){
        if((int)$char){
            $digit .= $char;
        }else{
            if(!$digit){
                $digit = "1";
            }
            $qte = (int)$digit;
            $digit = "";
            $decoded .= str_repeat($char, $qte);
        }
    }
    return $decoded;
}
