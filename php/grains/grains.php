<?php
/*
Here my lazy gmp_pow solution
i guess the main purpose  of the exercise is to write
our own implementation of an arbitrary bit width integer and operation
I need to learn more about binary maths before :)
 */
function validate($i)
{
    if (($i < 1) || ($i > 64)) {
        throw new InvalidArgumentException("Pas dans les clous");
    }
}

function square(int $i)
{
    validate($i);
    return (string) gmp_pow(2, ($i - 1));
}

function total(int $i = 64)
{
    validate($i);
    return (string) (gmp_pow(2, $i) - 1);
}
