<?php

class Bob
{
    public function respondTo($input)
    {
        $talk = trim($input);
        if ($this->question($talk) && $this->shout($talk)) {
            return "Calm down, I know what I'm doing!";
        } elseif ($this->question($talk)) {
            return 'Sure.';
        } elseif ($this->shout($talk)) {
            return 'Whoa, chill out!';
        } elseif ($this->silence($talk)) {
            return 'Fine. Be that way!';
        } else {
            return 'Whatever.';
        }
    }

    protected function shout($talk)
    {
        return strtoupper($talk) == $talk
        && !$this->noLetters($talk)
        && !$this->silence($talk);
    }

    protected function silence($talk)
    {
        return !$talk;
    }

    protected function noLetters($talk)
    {
        return !preg_match('/[a-zA-Z]/', $talk)
        && preg_match('/[0-9:)]/', $talk);
    }

    protected function question($talk)
    {
        return substr($talk, -1) == '?';
    }
}
