<?php

class Triangle
{
    public function __construct($a, $b, $c)
    {
        $sides = [$a, $b, $c];

        if (!array_sum($sides)) {
            throw new Exception("No size is illegal");
        }

        sort($sides);
        if (($sides[0] + $sides[1]) < $sides[2]) {
            throw new Exception("Triangle inequality mof'");
        }

        $same = array_unique($sides);

        $kinds = [
            1 => "equilateral",
            2 => "isosceles",
            3 => "scalene",
        ];

        $this->kind = $kinds[count($same)];
    }

    public function kind()
    {
        return $this->kind;
    }
}

if (!debug_backtrace()) {
    new Triangle(1, 3, 1);
}
