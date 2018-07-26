#!/usr/bin/env bash

input="$@"
r="" # init result

if [[ $(echo "$input % 3" | bc) -eq 0 ]]
then
    a="Pling"
    r=$r$a
fi

if [[ $(echo "$input % 5" | bc) -eq 0 ]]
then
    a="Plang"
    r=$r$a
fi

if [[ $(echo "$input % 7" | bc) -eq 0 ]]
then
    a="Plong"
    r=$r$a
fi

# if not %3 %5 nor %7 then just return the input
if [[ ${#r} -eq 0 ]]
then
    r="$input"
fi

echo "$r"
exit