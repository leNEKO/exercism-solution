<?php
// Bof …
class BeerSong{
    function verse(int $i){
        $verse = [
            ucfirst("{$this->bottles($i)} on the wall, {$this->bottles($i)}."),
            ucfirst("{$this->take($i)}, {$this->bottles($i-1)} on the wall."),
        ];
        return implode("\n",$verse) . (($i > 0) ? "\n" : "");
    }

    function bottles(int $i){
        $i = $i >= 0 ? $i : 99;
        return (
            ($i > 0) ? $i : "no more"
        ) . " bottle" . (
            ($i > 1 || $i == 0) ? "s" : ""
        ) . " of beer";
    }

    function take(int $i){
        if($i > 0){
            return "take " . ( ($i > 1) ? "one" : "it" ) . " down and pass it around";
        }else{
            return "go to the store and buy some more";
        }
    }

    function verses(int $s, int $e){
        $verses = [];
        foreach(range($s,$e) as $i){
            $verses[] = $this->verse($i);
        }
        return implode("\n", $verses);
    }

    function lyrics(){
        return $this->verses(99,0);
    }
}

if(!debug_backtrace()){
    $s = new BeerSong();
    print($s->verses(99,98));
}