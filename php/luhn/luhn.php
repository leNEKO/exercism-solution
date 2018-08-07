<?php

function isValid(string $card_num): bool
{
    # normalizing input
    $nospace = preg_replace("/\s/", "", $card_num);
    $digits = strrev(preg_replace("/\D/", "", $card_num));

    if (
        (strlen($digits) < 2) # must be at least 2 digits
         || (strlen($digits) != strlen($nospace)) # must be digits only
    ) {
        return false;
    }

    # init the check sum
    $checksum = 0;
    foreach (str_split($digits) as $k => $i) {
        switch ($k % 2) {
            case 0: # even positions
                $add = $i;
                break;
            case 1: # odd positions
                $double = $i * 2;
                $add = ($double > 9) ? ($double - 9) : $double; # if double > 9
                break;
        }
        $checksum += $add;
    }

    return ($checksum % 10) == 0;
}

if (!debug_backtrace()) {
    isValid("091");
}
