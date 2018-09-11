<?php
function from(DateTime $date): DateTime
{
    return (clone $date)->add(
        DateInterval::createFromDateString(1e9 . " seconds")
    );
}
