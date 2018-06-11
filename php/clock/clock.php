<?php
function mymod(int $i, $div){
    $a = intdiv($i, $div);
    $mod = $i % $div;
    if($mod < 0){
        $mod += abs($div);
    }
    return [$a, $mod];
}

class Clock{
    public $h,$m;

    function __construct(int $h, int $m = 0){
        $this->h = $h;
        $this->m = $m;
        $this->normalize();
    }

    function normalize(){
        // convert to minutes
        $day = 24 * 60;
        $tm = $this->h * 60 + $this->m;
        $tm = mymod($tm, $day)[1]; // wrap around days
        // convert back to h:m
        list($this->h, $this->m) = mymod($tm, 60);
    }

    function __toString(){
        $fmt = [
            str_pad($this->h, 2, "0", STR_PAD_LEFT),
            str_pad($this->m, 2, "0", STR_PAD_LEFT),
        ];
        return implode(":", $fmt);
    }

    function add(int $m){
        $this->m += $m;
        $this->normalize();
        return $this;
    }

    function sub(int $m){
        return $this->add($m * -1);
    }
}
