<?php
// don't do this at home kids solution
function calculate(string $q){

    var_dump($matches);

    $is_valid = !trim(preg_replace(array_keys($pats),"", $q));
    $to_evaluate = preg_replace(array_keys($pats), array_values($pats), $q);

    if($is_valid){
        eval("\$r = ($to_evaluate) ;");
        return $r;
    }

}

