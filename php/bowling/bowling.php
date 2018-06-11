<?php
// YAY ! all test passed
class Game{
    public $rolls = [];
    public $cur_roll = 0;

    public $frames = [];
    public $cur_frame = 0;

    function __construct(){
        // start with a new frame
        $this->new_frame();
    }

    function new_frame(){
        $this->cur_frame++;
        $frame = false;
        if($this->cur_frame < 10){
            $frame = new Frame($this);
        }elseif($this->cur_frame == 10){
            $frame = new TenthFrame($this);
        }
        if($frame){
            $this->frames[$this->cur_frame] = $frame;
        }
    }

    function roll(int $pins){
        if($pins < 0 || $pins > 10){
            throw new Exception("0 <= pins <= 10");
        }
        // rolls history
        $this->cur_roll++;
        $this->rolls[$this->cur_roll] = $pins;
        //  current frame
        $this->frames[$this->cur_frame]->roll($pins);
    }

    function score(): int{
        $total = 0;
        foreach($this->frames as $k => $frame){
            $total += $frame->score();
        }
        return $total;
    }
}

class CommonFrame{
    public $pins = 10;
    public $roll = 2;
    public $score = [];
    public $type = "UNFINISHED";

    protected $_parent;

    function __construct($parent){
        $this->_parent = $parent;
    }

    function roll(int $pins){
        $this->pins -= $pins;
        if($this->pins < 0){
            throw new Exception("ZEUS");
        }
        $this->roll --;
        $this->score[$this->_parent->cur_roll] = $pins;
    }

    function score(){
        if($this->type === "UNFINISHED"){
            throw new Exception("UNFINISHED");
        }
    }
}

class Frame extends CommonFrame{
    function roll($pins){
        parent::roll($pins);

        if(!$this->roll || !$this->pins){
            if(!$this->pins && $this->roll){
                $this->type = "STRIKE";
            }elseif(!$this->pins && !$this->roll){
                $this->type = "SPARE";
            }else{
                $this->type = "OPEN";
            }

            $this->_parent->new_frame();
        }
    }

    function score(){
        parent::score();
        $key = key($this->score);

        switch($this->type){
            case "STRIKE":
            case "SPARE":
                $length = 3;
                break;
            case "OPEN":
                $length = 2;
                break;
            default:
                $length = 0;
        }
        $slice = array_slice($this->_parent->rolls, $key-1, $length);

        return array_sum($slice);

    }
}


class TenthFrame extends CommonFrame{
    function __construct($parent){
        $this->bonus = 0;
        parent::__construct($parent);
    }

    function roll($pins){
        parent::roll($pins);

        // new frame if roll >=2 or no more pins
        if(!$this->roll || !$this->pins){
            if(!$this->pins && $this->roll){
                $this->type = "STRIKE";
                $this->pins = 10;
                $this->bonus = 1;
            }elseif(!$this->pins && !$this->roll){
                $this->type = "SPARE";
                $this->pins = 10;
                $this->bonus = 1;
            }else{
                $this->type = "OPEN";
            }
        }

        if($this->roll < 0 && !$this->bonus){
            throw new Exception("too much");
        }
    }

    function score(){
        parent::score();
        if($this->bonus && $this->roll != -1){
            throw new Exception("not enough");
        }
        if(!$this->bonus && count($this->score) > 2){
            array_pop($this->score);
        }
        $total =  array_sum($this->score);
        return $total;
    }
}
