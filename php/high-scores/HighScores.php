<?php

declare(strict_types=1);

class HighScores
{
    /** @var int[] */
    public array $scores;

    public function __construct(
        array $scores
    ) {
        $this->scores = $scores;
        $this->latest = \end($scores);

        \rsort($scores);
        $this->personalBest = \reset($scores);
        $this->personalTopThree = \array_slice($scores, 0, 3);
    }
}
