<?php
function from(DateTime $date): DateTimeImmutable
{
    $nu_date = DateTimeImmutable::createFromMutable($date);
    return $nu_date->add(
        DateInterval::createFromDateString(
            10 ** 9 . " seconds"
        )
    );
}
