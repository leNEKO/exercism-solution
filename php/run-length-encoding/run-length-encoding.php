<?php

// Regex only implementation is faster
use runLengthLoop as runLength;

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

if (!debug_backtrace()) {
    $cod = "AAAAAABBBBBBCCCCCCDDDDEFEFKZPEFEKP";
    $dec = encode($cod);
    var_dump([$cod, $dec, decode($dec)]);

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

    foreach (["runLengthLoop", "runLengthRegex"] as $n) {
        print("\n---- $n ----\n");

        # big file
        $cod = file_get_contents("alice.txt");
        $command = function () use ($n, $cod) {
            $dec = $n::encode($cod);
            $n::decode($dec);
        };
        print("big file: ");
        print(benchmark($command, 1));

        # small file
        $cod = "AAAAAABBBBBBCCCCCCDDDDEFEFKZPEFEKP";
        $command = function () use ($n, $cod) {
            $dec = $n::encode($cod);
            $n::decode($dec);
        };
        print("small file: ");
        print(benchmark($command, 10000));
        benchmark($command, 5000);
    }
}
