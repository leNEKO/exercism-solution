<?php

class Bob
{
    public function respondTo($question)
    {

        // unicode trim https://stackoverflow.com/questions/4166896
        $question = preg_replace('/^[\pZ\pC]+|[\pZ\pC]+$/u', '', $question);

        $score_of_answer = 0;

        if ($question == '') {
            return 'Fine. Be that way!';
        }

        if (substr($question, -1) == '?') {
            $score_of_answer += 1;
        }

        $yell_test_help = preg_replace('/[^[:alpha:]]/u', '', $question);

        if (
            $yell_test_help == mb_strtoupper($yell_test_help)
            && $yell_test_help != ''
        ) {
            $score_of_answer += 2;
        }

        $all_answers = array(0 => "Whatever.",
            1 => "Sure.",
            2 => "Whoa, chill out!",
            3 => "Calm down, I know what I'm doing!");

        return $all_answers[$score_of_answer];

    }
}
