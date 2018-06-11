<?php

function solve(string $board){
    $g = new Game($board);
    return $g->solved;
}

class Game{
    public $board = [];
    public $solved = "";

    function __construct($board){
        $lines = explode(
            "\n",
            trim($board)
        );

        // check for unequal board
        $cl = [];
        foreach($lines as $line){
            $cl[strlen(trim($line))] = true;
        }
        if(count($cl) > 1){
            throw new InvalidArgumentException("Unequal board");
        }

        // check for valid bounds
        $bounds = [
            array_shift($lines),
            array_pop($lines)
        ];
        foreach($bounds as $bound){
            if(!preg_match('/\+-{2,}\+/', $bound)){
                throw new InvalidArgumentException("Invalid start");
            }
        }

        // check for valid line then record Point
        foreach($lines as $y => $line){
            if(!preg_match("/\|(( |\*){2,})\|/", $line, $matches)){
                throw new InvalidArgumentException("Invalid line");
            }
            foreach(str_split($matches[1]) as $x => $val){
                $this->board["$x,$y"] = new Point($this, $x, $y, $val);
            }
        }

        // solve the minesweep
        $tab = [];
        foreach($this->board as $point){
            list($x,$y) = $point->coord;
            $tab[$y][$x] = $point->count_mines();
        }

        // draw solved
        $draw = [];
        $draw[] = array_shift($bounds);
        foreach($tab as $line){
            $draw[] = "|". implode("",$line) . "|";
        }
        $draw[] = array_pop($bounds);
        $this->solved = "\n" . implode("\n",$draw) . "\n";
    }
}

class Point{
    public $coord = [];
    public $val = "";
    private $parent;

    function __construct($parent, $x, $y, $val){
        $this->parent = $parent;
        $this->coord = [$x, $y];
        $this->val = $val;
    }

    function count_mines(){
        $board = $this->parent->board;
        list($x,$y) = $this->coord;

        // if is a mine
        if($this->val === "*"){
            return "*";
        }

        $mines = 0;
        $coords = [];
        foreach(range(-1,1) as $ox){
            foreach(range(-1,1) as $oy){
                $nx = $x + $ox;
                $ny = $y + $oy;
                $coords[] = "$nx,$ny";
            }
        }

        foreach(array_unique($coords) as $coord){
            if(isset($board[$coord])){
                $point = $board[$coord];
                $mines += $point->val === "*";
            }
        }

        // return space instead of 0
        return $mines ?: " ";
    }
}
