<?php
/*
oh well this is a copy of the implementation of Uncle Bob that figures in his ppt file
http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata

Worse result than my first attempt
*/
class Game {
    public $rolls = [];
    public $currentRoll = 0;

    function roll(int $pins){
        if($pins < 0 || $pins > 10){
            throw new Exception();
        }
        $this->rolls[$this->currentRoll++] = $pins;
    }

    function score(){
        $score = 0;
        $frameIndex = 0;
        for($frame = 0; $frame < 10; $frame++) {
            if($this->isStrike($frameIndex)) {
                $score += 10 + $this->strikeBonus($frameIndex);
                $frameIndex++;
            } else if ($this->isSpare($frameIndex)) {
                $score += 10 + $this->spareBonus($frameIndex);
                $frameIndex += 2;
            } else {
                $score += $this->sumOfBallsInFrame($frameIndex);
                $frameIndex += 2;
            }
        }
        return $score;
    }

    function isStrike(int $frameIndex) {
        return $this->rolls[$frameIndex] == 10;
    }

    function sumOfBallsInFrame(int $frameIndex) {
        $sum = $this->rolls[$frameIndex] + $this->rolls[$frameIndex+1];
        if($sum > 10){
            throw new Exception();
        }else{
            return $sum;
        }
    }

    function spareBonus(int $frameIndex) {
        return $this->rolls[$frameIndex+2];
    }

    function strikeBonus(int $frameIndex) {
        return $this->rolls[$frameIndex+1] + $this->rolls[$frameIndex+2];
    }

    function isSpare(int $frameIndex) {
        return ($this->rolls[$frameIndex] + $this->rolls[$frameIndex+1]) == 10;
    }
}