<?php

function transform($legacy)
{
    $nu = [];
    foreach ($legacy as $score => $letters) {
        foreach ($letters as $letter) {
            $nu[strtolower($letter)] = $score;
        }
    }
    return $nu;
}
