<?php
// so much reverse reverse, must be some cleverer way …
function vlq_encode(array $ints)
{
    $output = [];

    foreach ($ints as $int) {
        $chunks = str_split(strrev(decbin($int)), 7); // split as 7 bit chunks (reversed)

        foreach ($chunks as $k => $val) {
            $msb = $k ? "1" : "0"; // the MSB will be 0 only for the first chunk
            $part = strrev($val); // reversed back part of the message
            $padded = str_pad($part, 7, "0", STR_PAD_LEFT); // pad missing 0
            $chunks[$k] = $msb . $padded; // 8 bit chunk
        }
        // so we reverse the chunks array to have it in the right order
        foreach (array_reverse($chunks) as $bin) {
            $output[] = bindec($bin);
        }
    }

    return $output;
}

function vlq_decode(array $ints)
{
    $output = [];
    $message = "";

    foreach ($ints as $int) {
        $padded = str_pad(decbin($int), 8, "0", STR_PAD_LEFT);
        $msb = substr($padded, 0, 1);
        $message .= substr($padded, 1);

        if (strlen($message) > 32) {
            throw new \OverflowException("Wow too big");
        }

        if (!$msb) {
            $output[] = bindec($message);
            $message = "";
        }
    }

    if ($message) {
        throw new \InvalidArgumentException("Incomplete message");
    }

    return $output;
}

// wow, that was kinda painful
