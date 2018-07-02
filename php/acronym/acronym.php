<?php

function acronym(string $str): string
{
    preg_match_all("/(\b(\w)|([A-Z])[a-z])/u", $str, $matches);
    foreach ($matches[2] as $k => $val) {
        $matches[2][$k] .= $matches[3][$k];
    }
    $acronym = mb_strtoupper(implode("", $matches[2]));
    return strlen($acronym) > 1 ? $acronym : "";
}

// if(main) :)
if (!debug_backtrace()) {
    acronym('HyperText Markup Language');
}
