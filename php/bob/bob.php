<?php
// added support for utf-8 and other whitespaces

class Bob
{
    public function respondTo(string $message): string
    {
        // chars
        preg_match_all('/[[:alnum:][:punct:]]/u', $message, $matches);
        $chars = implode("", $matches[0]);

        // alphas
        preg_match_all('/[[:alpha:]]/u', $message, $matches);
        $alpha = implode("", $matches[0]);

        // if nothing said no need to go further
        if ($chars === "") {
            return "Fine. Be that way!";
        }

        # sentence properties
        $is_question = substr($chars, -1) === "?";
        $is_upper = $alpha && (mb_strtoupper($alpha) === $alpha);

        $response = "Whatever.";
        if ($is_question && $is_upper) {
            $response = "Calm down, I know what I'm doing!";
        } elseif ($is_upper) {
            $response = "Whoa, chill out!";
        } elseif ($is_question) {
            $response = "Sure.";
        }

        return $response;
    }
}

if (!debug_backtrace()) {
    $b = new Bob();
    var_dump($b->respondTo("1,2,3 ?"));
}
