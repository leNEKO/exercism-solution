<?php
// i just translated my python solution
function sieve($limit){
    $nums = range(0,$limit);
    $nums[1] = 0;

    foreach($nums as $i){
        if($i){
            // forgot to start at $i ** 2
            for($y = $i ** 2 ; $y <= $limit; $y += $i){
                $nums[$y] = 0;
            }
        }
    }

    return array_values( // reset the keys
        array_filter($nums, function($val){
            if($val){ // filter out the 0
                return $val;
            }
        })
    );
}
