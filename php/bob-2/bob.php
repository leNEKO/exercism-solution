<?php
// added support for utf-8 and other whitespaces

class Bob
{
    private $brain = [
        0b100 => "Sure.",
        0b010 => "Whoa, chill out!",
        0b110 => "Calm down, I know what I'm doing!",
        0b111 => "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn",
        0b001 => "Fine. Be that way!",
        0b000 => "Whatever.",
    ];

    public function respondTo(string $message): string
    {
        // normalized
        $normalized = trim(preg_replace("/[^[:alnum:]\?]/u", "", $message));

        // nothing
        if (!$normalized) {
            return $this->brain[0b001];
        }

        // anything
        $state = 0b000;

        // question
        if ($normalized[-1] === "?") {
            $state += 0b100;
        }

        // yelling
        $letters = preg_replace("/[^[:alpha:]]/u", "", $message);
        $upper = mb_strtoupper($letters);
        if ($letters && ($letters === $upper)) {
            $state += 0b010;
        }

        return $this->brain[$state];
    }
}

if (!debug_backtrace()) {
    $b = new Bob();
    var_dump($b->respondTo("1,2,3"));
}
