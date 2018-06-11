<?php

function toDecimal(string $str, int $mode = 3){
    $pos = str_split(
        strrev(trim($str))
    );
    $total = 0;
    foreach($pos as $pow => $val){
        if($val < $mode){
            $total += $val * ($mode ** $pow);
        }else{
            return 0;
        }
    }
    return $total;
}