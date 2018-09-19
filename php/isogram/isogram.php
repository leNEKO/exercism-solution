<?php
// common code
function normalize(string $str): array
{
    $lower = mb_strtolower($str);
    preg_match_all('/\w/u', $lower, $matches);
    return $matches[0];
}

// faster approach seems to be the one using array_unique
function isIsogram(string $str): bool
{
    return isIsogramUniq($str);
}

// splitting string instead of preg_match_all is slightly slower
function isIsogramUniqSplit(string $str): bool
{
    $str = preg_replace('/\s+/', '', $str);
    $chars = preg_split('//u', mb_strtolower($str), null, PREG_SPLIT_NO_EMPTY);
    return array_unique($chars) === $chars;
}

// faster approach
function isIsogramUniq(string $str): bool
{
    $chars = normalize($str);

    return array_unique($chars) === $chars;
}

// shortcircuit a for loop is not faster than array_uniq
function isIsogramLoopInarray(string $str): bool
{
    $chars = normalize($str);

    $been_found = [];
    foreach ($chars as $char) {
        if (in_array($char, $been_found, true)) {
            return false;
        }
        $been_found[] = $char;
    }
    return true;
}
// checking if isset(…) seems faster than in_array(…)
function isIsogramLoopIsset(string $str): bool
{
    $chars = normalize($str);

    $been_found = [];
    foreach ($chars as $char) {
        if (isset($been_found[$char])) {
            return false;
        }
        $been_found[$char] = true;
    }
    return true;
}

// reduce is way slower
function isIsogramReduce(string $str): bool
{
    $chars = normalize($str);

    $been_found = [];
    $check = function (bool $is_isogram, string $char) use (&$been_found) {
        $found = isset($been_found[$char]);
        $been_found[] = $char;
        return $is_isogram && !$found;
    };

    return array_reduce($chars, $check, true);
}

function isIsogramCountFilter(string $str): bool
{
    $chars = normalize($str);

    $counted = array_count_values($chars);
    $isnot_isogram = function (int $v) {
        return $v > 1;
    };

    return (bool) !array_filter($counted, $isnot_isogram);
}

function isIsogramCountLoop(string $str): bool
{
    $chars = normalize($str);

    foreach (array_count_values($chars) as $v) {
        if ($v > 1) {
            return false;
        }
    };
    return true;
}

function isIsogramStudent(string $input)
{
    if (strlen($input) === 0) {
        return false;
    }
    // $alphabet = array_flip(str_split('abcdefghijklmnopqrstuvwxyz'));
    $lower = mb_strtolower($input);
    preg_match_all("/\w/u", $lower, $m);
    $test = $m[0];
    $alphabet = [];

    foreach ($test as $char) {
        if (isset($alphabet[$char])) {
            return false;
        }
        $alphabet[$char] = true;
    }
    return true;
}

if (!debug_backtrace()) {
    # benchmarking
    function benchmark(\Closure $action, $times = 1000)
    {
        $chrono_start = microtime(true);
        for ($i = 0; $i < $times; $i++) {
            $action();
        }
        $chrono_end = microtime(true);
        return ($chrono_end - $chrono_start) / $times;
    }

    $txt = 'Heizölrückstoßabdämpfung';

    $i = 10000; // benchmarking iterations
    $methods = [
        "isIsogramUniq",
        "isIsogramUniqSplit",
        "isIsogramLoopInarray",
        "isIsogramLoopIsset",
        "isIsogramReduce",
        "isIsogramCountFilter",
        "isIsogramCountLoop",
        "isIsogramStudent",
    ];

    $r = [];
    foreach ($methods as $m) {
        $func = function () use ($txt, $m) {
            return $m($txt);
        };
        $r[$m] = benchmark($func, $i);
    }
    asort($r);

    $n = 0;
    foreach ($r as $m => $dur) {
        $n++;
        $t = $dur * 1e6;
        echo "#{$n} - $m :\n$t µs.\n\n";
    }
}
