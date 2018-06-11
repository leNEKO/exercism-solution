<?php
/*
My first attemp
so much pain and shame here … 5 failures / 24 tests
bad design, i need to read other solutions …
*/

Class Game{
    public $frame;

    public $roll;
    public $pins;

    public $scores;
    public $keys;

    function __construct(){
        $this->new_frame();
    }

    function new_frame(){
        if($this->frame < 10){
            $this->frame++;
            $this->roll = 0;
            $this->pins = 10;
        }else{
            $this->pins = 10;
        }
    }

    function roll(int $pins){
        $this->current[] = $pins;
        $this->roll ++;
        $this->pins -= $pins;

        $error["too_much"] = $this->pins < 0;
        $error["too_many"] = $pins > 10;
        $error["not_enough"] = $pins < 0;;

        foreach($error as $k => $val){
            if($val){
                throw new Exception($k);
            }
        }

        $key = "{$this->frame}.{$this->roll}"; // key name

        if(!$this->pins && $this->roll === 1){ // strike!
            $this->new_frame();
        }elseif($this->roll === 2){
            $this->new_frame();
        }

        // record score
        $this->scores[$key] = $pins;
        $this->keys[] = $key;
    }

    function score_slice($vkey_start, $vkey_stop = false){
        if($vkey_stop === false){
            $vkey_stop = $vkey_start;
        }
        $scores = [];
        foreach(range($vkey_start, $vkey_stop) as $vkey){
            if(isset($this->keys[$vkey])){
                $key = $this->keys[$vkey];
                $scores[] = $this->scores[$key];
            }
        }
        return $scores;
    }

    function score($print = false){
        if(
            ($this->frame < 10)
            && ($this->roll < 2)

        ){
            throw new Exception("Not started");
        }
        $scores = $this->scores;
        $keys = $this->keys;

        $total = 0;
        foreach($keys as $vkey => $key){
            list($frame, $roll) = explode(".", $key);

            // Scores
            $score = $scores[$key];
            // surrounding;
            $prevs = $this->score_slice($vkey - 1);
            $nexts = $this->score_slice($vkey + 1, $vkey + 2);

            $total += $score;

            $spec = "OPEN";

            if($frame < 10){
                // STRIKE
                if($score === 10){
                    $spec = "STRIKE!";
                    $total += array_sum($nexts);
                }
                // SPARE!
                if(
                    (int)$roll === 2
                    && ($score + $prevs[0]) === 10
                ){
                    $spec = "SPARE!";
                    $total += $nexts[0];
                }
            }

            if($print){
                var_dump("#$frame.$roll score:$score - $spec total: $total ");
            }
        }
        return $total;
    }
}