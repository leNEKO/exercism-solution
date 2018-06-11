<?php

function resultFor(array $board){
    $g = new Game($board);

    $map = [
        "X" => "black",
        "O" => "white"
    ];

    // 1 x 1 game
    if($g->w === 0 && $g->h === 0){
        return $map[$g->board["0,0"]->value];
    }

    // TODO: DRY this
    foreach($g->board as $point){
        // check for X
        if($point->coord[0] === 0 && $point->value === "X"){
            // :( my wtf way of caught the recursion result
            ob_start();
                $point->follow();
            $data = ob_get_clean();

            if(preg_match("/X $g->w,./",$data)){
                return $map["X"];
            }
        }
        // check for O
        if($point->coord[1] === 0 && $point->value === "O"){
            ob_start();
                $point->follow();
            $data = ob_get_clean();

            if(preg_match("/O .,$g->h/",$data)){
                return $map["O"];
            }
        }
    }
}

class Game{
    public $board = [];
    public $w;
    public $h;

    function __construct(array $board){
        // record each point
        foreach($board as $y => $line){
            $c = preg_replace("/\s+/","",$line);
            $x = 0;
            foreach(str_split($c) as $char){
                $this->board["$x,$y"] = new Point($this, $x, $y, $char);
                $x++;
            }
        }

        // the board dimension
        $this->w = strlen($c) - 1;
        $this->h = count($board) - 1;

        // update points with their neighbors
        foreach($this->board as $point){
            $point->neighboorhood();
        }
    }
}

class Point{
    public $coord = [];
    public $value = "";
    public $neighbors = [];
    public $path = [];

    private $parent;

    function __construct($parent, $x, $y, $value){
        $this->parent = $parent;
        $this->coord = [$x, $y];
        $this->value = $value;
    }

    // record surounding points that have same value
    function neighboorhood(){
        list($x, $y) = $this->coord;
        $board = $this->parent->board;

        $directions = [
            [$x-1, $y],
            [$x-1, $y+1],
            [$x, $y-1],
            [$x, $y+1],
            [$x+1, $y-1],
            [$x+1, $y]
        ];

        foreach($directions as $direction){
            list($dx,$dy) = $direction;
            if(isset($board["$dx,$dy"])){
                if($board["$dx,$dy"]->value == $this->value){
                    $this->neighbors[] = $board["$dx,$dy"];
                }
            }
        }
    }

    // recursive function done "badly"
    public function follow(){
        foreach($this->neighbors as $point){
            if(!in_array($point, $this->path)){
                list($x,$y) = $point->coord;
                print("{$this->value} $x,$y\n"); // oh i am so sure there is a better way to do this ...
                $this->path[] = $point; // do this point once
                $point->follow();
            }
        }
    }

}