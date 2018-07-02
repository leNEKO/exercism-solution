<?php
function accumulate(array $input, callable $accumulator): array
{
    $output = [];
    foreach ($input as $val) {
        $output[] = $accumulator($val);
    }
    return $output;
}
