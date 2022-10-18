<?php

declare(strict_types=1);

enum Score: int
{
    case WIN = 1;
    case LOSS = -1;
    case DRAW = 0;

    public static function fromString(string $string): self
    {
        return match ($string) {
            'win' => static::WIN,
            'loss' => static::LOSS,
            'draw' => static::DRAW,
        };
    }

    public function points(): int
    {
        return match ($this) {
            static::WIN => 3,
            static::DRAW => 1,
            static::LOSS => 0,
        };
    }

    /** WIN -> LOSS ; LOSS -> WIN :) */
    public function invert(): self
    {
        return static::from($this->value * -1);
    }
}

class ScoreCounter
{
    private array $data;

    public function increment(Score $score): int
    {
        $this->data[$score->name] ??= 0;

        return ++$this->data[$score->name];
    }

    public function get(Score $score): int
    {
        return $this->data[$score->name] ?? 0;
    }
}

class Report
{
    const FORMAT = '%-30s | %+2s | %+2s | %+2s | %+2s | %+2s';

    public function __construct(
        public string $teamName,
        public int $matchPlayed,
        public int $win,
        public int $draw,
        public int $loss,
        public int $points,
    ) {
    }

    public function expose(): string
    {
        return \sprintf(
            static::FORMAT,
            $this->teamName,
            $this->matchPlayed,
            $this->win,
            $this->draw,
            $this->loss,
            $this->points
        );
    }

    public static function head(): string
    {
        return \sprintf(
            static::FORMAT,
            'Team',
            'MP',
            'W',
            'D',
            'L',
            'P'
        );
    }
}

class Tournament
{
    /** @param array<Score[]> */
    private array $teams = [];

    public function tally(string $input)
    {
        $this->load($input);

        return $this->expose();
    }

    private function load(string $input): void
    {
        if ('' === \trim($input)) {
            return;  # early return if nothing to load
        }

        $lines = \explode(PHP_EOL, $input);

        foreach ($lines as $line) {
            [$localTeam, $visitorTeam, $scoreString] = \explode(';', $line);

            $score = Score::fromString($scoreString);

            $this->teams[$localTeam][] = $score;
            $this->teams[$visitorTeam][] = $score->invert();  # a win for local is a loss for visitor
        }
    }

    private function expose(): string
    {
        $reports = \array_map(
            fn (string $name, array $value): Report => static::calc($name, $value),
            \array_keys($this->teams),
            \array_values($this->teams)
        );

        \usort(
            $reports,
            function (Report $a, Report $b): int {
                if ($a->points === $b->points) {  # if equality
                    return $a->teamName <=> $b->teamName;  # sort by team name ASC 
                }

                return $b->points <=> $a->points;  # sort by points DESC
            }
        );

        return \implode(
            PHP_EOL,
            [
                Report::head(),
                ...\array_map(
                    fn (Report $report): string => $report->expose(),
                    $reports
                )
            ]
        );
    }

    /** @param Score[] $scores */
    private static function calc(string $teamName, array $scores): Report
    {
        $matchPlayed = \count($scores);
        $counter = new ScoreCounter();
        $points = 0;

        foreach ($scores as $score) {
            $counter->increment($score);
            $points += $score->points();
        }

        return new Report(
            $teamName,
            $matchPlayed,
            $counter->get(Score::WIN),
            $counter->get(Score::DRAW),
            $counter->get(Score::LOSS),
            $points
        );
    }
}
