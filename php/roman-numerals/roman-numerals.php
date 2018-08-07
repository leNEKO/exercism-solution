<?php
function toRomanMe(int $i)
{
    $system = [
        1000 => "M",
        900 => "CM",
        500 => "D",
        400 => "CD",
        100 => "C",
        90 => "XC",
        50 => "L",
        40 => "XL",
        10 => "X",
        9 => "IX",
        5 => "V",
        4 => "IV",
        1 => "I",
    ];

    $roman = "";

    foreach ($system as $val => $k) {
        while (($i - $val) >= 0) {
            $roman .= $k;
            $i -= $val;
        }
    }

    return $roman;
}

function toRoman($input)
{
    $romanNumerals = initRomanNumerals();

    $arrayOfDigits = splitByDigits($input);

    $result = '';
    foreach ($arrayOfDigits as $digit) {
        $romanString = '';
        $isSpecial = checkIsFourOrNine($digit[0]);

        while ($digit > 0) {
            foreach ($romanNumerals as $modern => $roman) {
                next($romanNumerals);
                if ($digit >= $modern && ($digit < key($romanNumerals)) || is_null(key($romanNumerals))) {
                    if (checkIsFourOrNine($digit[0])) {
                        $romanString = current($romanNumerals) . $romanString;
                    } elseif ($isSpecial) {
                        $romanString = $roman . $romanString;
                    } else {
                        $romanString .= $roman;
                    }

                    if (checkIsFourOrNine($digit[0])) {
                        $digit = key($romanNumerals) - $digit;
                    } else {
                        $digit -= $modern;
                    }

                    reset($romanNumerals);
                    break;
                }
            }
        }

        $result .= $romanString;
    }

    return $result;
}

function splitByDigits($number)
{
    $result = str_split((string) $number);

    end($result);

    $length = key($result);

    array_walk($result, function (&$item, $key) use ($length) {
        while ($length != $key) {
            $item .= '0';
            $length--;
        }
    });

    return $result;
}

function checkIsFourOrNine($digit)
{
    return $digit == 4 || $digit == 9;
}

function initRomanNumerals()
{
    return [
        1 => 'I',
        5 => 'V',
        10 => 'X',
        50 => 'L',
        100 => 'C',
        500 => 'D',
        1000 => 'M',
    ];
}
