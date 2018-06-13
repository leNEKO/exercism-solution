<?php

function findFewestCoins(array $coins, int $amount){
    rsort($coins);

    if(!$amount){
        return [];
    }

    if($amount < min($coins)){
        throw new InvalidArgumentException("No coins small enough to make change");
    }

    $best = false;
    for($i = count($coins); $i > 1; $i --){
        $conf = array_slice($coins, -$i);
        $change = [];
        $total = $amount;
        foreach($conf as $val){
            while(($total - $val) >= 0){
                $change[] = $val;
                $total -= $val;
            }
        }

        if(!$best || count($change) < count($best)){
            $best = $change;
        }
    }
    sort($best);
    return $best;
}
