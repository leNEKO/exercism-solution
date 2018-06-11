<?php
function distance($a, $b)
{
    if(strlen($a) != strlen($b)){
        throw new InvalidArgumentException('DNA strands must be of equal length.');
    }

    $m = 0;
    foreach(str_split($a) as $k => $c){
        if($b[$k] != $c){
            $m++;
        }
    }
    return $m;

}