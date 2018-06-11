<?php
ini_set('display_errors', 1);
error_reporting(~0);

include "bowling.php";

class test{
    function __construct(){
        $this->game = new Game();
        var_dump($this->game);
    }

    private function rollMany($n, $pins)
    {
        for ($i = 0; $i < $n; $i++) {
            $this->game->roll($pins);
        }
    }
}


new Test();