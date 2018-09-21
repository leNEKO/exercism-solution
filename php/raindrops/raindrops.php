<?php
function raindrops(int $i): string
{
    $r = "";
    if ($i % 3 == 0) {
        $r .= "Pling";
    }

    if ($i % 5 == 0) {
        $r .= "Plang";
    }

    if ($i % 7 == 0) {
        $r .= "Plong";
    }

    if ($r == "") {
        $r = (string) $i;
    }

    return $r;
}
