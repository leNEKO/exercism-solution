<?php
function raindrops(int $i): string{
    $r = "";
    $r .= ($i % 3 == 0) ? "Pling" : "";
    $r .= ($i % 5 == 0) ? "Plang" : "";
    $r .= ($i % 7 == 0) ? "Plong" : "";
    $r = $r ?: (string)$i;
    return $r;
}