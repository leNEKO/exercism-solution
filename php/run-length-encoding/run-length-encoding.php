<?php

// Regex only implementation is faster
use runLengthStudent as runLength;

function encode($input): string
{
    return runLength::encode($input);
}
function decode($input): string
{
    return runLength::decode($input);
}

class runLengthLoop
{

    public static function encode($input): string
    {

        $encoded = "";
        $last_char = "";
        $counter = 1;

        foreach (str_split($input . " ") as $char) {
            $same = $char === $last_char;
            $counter += (int) $same;
            if (!$same) {
                $encoded .= ($counter > 1) ? $counter : "";
                $encoded .= $last_char;
                $counter = 1; # reset counter
            }
            $last_char = $char;
        }

        return $encoded;
    }

    public static function decode($input): string
    {
        $decoded = "";
        $digit = "";

        foreach (str_split($input) as $char) {
            if ((int) $char) {
                $digit .= $char;
            } else {
                if (!$digit) {
                    $digit = "1";
                }
                $decoded .= str_repeat($char, (int) $digit);
                $digit = ""; # reset digit
            }
        }
        return $decoded;
    }

}

class runLengthRegex
{
    public static function encode($input): string
    {
        // callback
        $c = function ($m) {
            $l = strlen($m[0]);
            $d = $l > 1 ? $l : '';
            return $d . $m[1];
        };
        return preg_replace_callback('/(.)\1*/', $c, $input);
    }

    public static function decode($input): string
    {
        // callback
        $c = function ($m) {
            return str_repeat($m[2], $m[1]);
        };
        return preg_replace_callback('/(\d+)(\D)/', $c, $input);
    }
}

class runLengthStudent
{
    public function encode($input)
    {
        $count = 1;
        $compare = '';
        $output = '';

        if (!$input) {
            return '';
        }

        foreach (str_split($input) as $char) {

            if ($char === $compare) {
                $count++;
            } else {
                if ($count > 1) {
                    $output .= $count;
                }
                $output .= $compare;
                $count = 1;
            }

            $compare = $char;
        }

        if ($count > 1) {
            $output .= $count;
        }

        $output .= $char;

        return $output;
    }

    public function decode($input)
    {
        $output = '';

        preg_match_all('/([1-9]*)(\w|\s)/', $input, $matches);

        for ($index = 0; $index < count($matches[0]); $index++) {
            $count = $matches[1][$index];

            if ($count === '') {
                $count = 1;
            }

            $char = $matches[2][$index];
            $output .= str_repeat($char, (int) $count);
        }

        return $output;
    }
}

if (!debug_backtrace()) {
    # benchmarking
    function benchmark($callback, $i = 100)
    {
        $time_start = microtime(true);
        while ($i) {
            $callback();
            $i--;
        }
        $time_end = microtime(true);
        $duration = round(($time_end - $time_start) * 1000, 2);

        return "$duration ms.\n";
    }

    $implementations = [
        "runLengthLoop",
        "runLengthRegex",
        "runLengthStudent",
    ];

    $small_data = "AAAAAABBBBBBCCCCCCDDDDEFEFKZPEFEKP";
    $big_data = file_get_contents("alice.txt");

    foreach ($implementations as $n) {
        print("\n---- $n ----\n");

        # big file
        $command = function () use ($n, $big_data) {
            $dec = $n::encode($big_data);
            $n::decode($dec);
        };
        print("big file: ");
        print(benchmark($command, 5));

        # small file
        $command = function () use ($n, $small_data) {
            $dec = $n::encode($small_data);
            $n::decode($dec);
        };
        print("small file: ");
        print(benchmark($command, 50000));
    }
}
