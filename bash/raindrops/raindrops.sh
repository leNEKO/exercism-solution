#!/usr/bin/env bash

input="$@"
res="" # init result

if [[ $(echo "$input % 3" | bc) -eq 0 ]]
then
    add="Pling"
    res=$res$add
fi

if [[ $(echo "$input % 5" | bc) -eq 0 ]]
then
    add="Plang"
    res=$res$add
fi

if [[ $(echo "$input % 7" | bc) -eq 0 ]]
then
    add="Plong"
    res=$res$add
fi

# if not %3 %5 nor %7 then just return the input
if [[ ${#res} -eq 0 ]]
then
    res="$input"
fi

echo "$res"
exit