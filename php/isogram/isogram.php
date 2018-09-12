<?php
// faster approach seems to be the one using array_unique
function isIsogram(string $str): bool
{
    return isIsogramUniq($str);
}

// faster approach
function isIsogramUniq(string $str): bool
{
    $lower = mb_strtolower($str);
    preg_match_all('/\w/u', $lower, $matches);
    $chars = $matches[0];
    return array_unique($chars) == $chars;
}
// split is slightly slower
function isIsogramUniqSplit(string $str): bool
{
    $str = preg_replace('/\s+/', '', $str);
    $chars = preg_split('//u', mb_strtolower($str), null, PREG_SPLIT_NO_EMPTY);
    return array_unique($chars) == $chars;
}

// shortcircuit a foor loop is not faster than array_uniq
function isIsogramLoop(string $str): bool
{
    $lower = mb_strtolower($str);
    preg_match_all('/\w/u', $lower, $matches);
    $c = [];
    foreach ($matches[0] as $char) {
        if (in_array($char, $c)) {
            return false;
        }
        $c[] = $char;
    }
    return true;
}

// reduce is way slower
function isIsogramReduce(string $str): bool
{
    $lower = mb_strtolower($str);
    preg_match_all('/\w/u', $lower, $matches);
    $chars = $matches[0];
    $arr = [];
    $check = function ($x, $y) use (&$arr) {
        $rtn = in_array($y, $arr);
        $arr[] = $y;
        return $x && !$rtn;
    };
    return array_reduce($chars, $check, true);
}

if (!debug_backtrace()) {
    # benchmarking
    function benchmark($action, $times = 1000)
    {
        $time_start = microtime(true);
        while ($times) {
            $action();
            $times--;
        }
        $time_end = microtime(true);
        $duration = round(($time_end - $time_start) * 1000, 2);
        print("$duration ms.\n");
    }

    $txt = 'Heizölrückstoßabdämpfung';
    $loop_test = function () use ($txt) {
        return isIsogramLoop($txt);
    };

    $uniq_test = function () use ($txt) {
        return isIsogramUniq($txt);
    };
    $uniq_split_test = function () use ($txt) {
        return isIsogramUniqSplit($txt);
    };

    $reduce_test = function () use ($txt) {
        return isIsogramReduce($txt);
    };

    $i = 10000;
    benchmark($uniq_test, $i);
    benchmark($uniq_split_test, $i);
    benchmark($loop_test, $i);
    benchmark($reduce_test, $i);
}
