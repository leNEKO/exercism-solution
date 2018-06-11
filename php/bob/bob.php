<?php
class Bob{
    private $brain = [
        0b100 => "Sure.",
        0b010 => "Whoa, chill out!",
        0b110 => "Calm down, I know what I'm doing!",
        0b111 => "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn",
        0b001 => "Fine. Be that way!",
        0b000 => "Whatever."
    ];

    function respondTo(string $message): string{
        $message = trim($message);
        $state = 0b000;
        // anything
        if(!$message){
            $state += 0b001;
        }else{
            // question
            if($message[-1] === "?"){
                $state += 0b100;
            }
            // yelling
            $letters = preg_replace('/[^A-Za-z]/','',$message);
            if($letters && (strtoupper($letters) === $letters)){
                $state += 0b010;
            }
        }

        return $this->brain[$state];

    }
}
