#!/usr/bin/env bash

input="$@"
res="" # init result

PRIME_TO_SOUND=(
    [3]=Pling
    [5]=Plang
    [7]=Plong
)

for k in "${!PRIME_TO_SOUND[@]}"
do
    if (( input % k == 0 ))
    then
        res=$res${PRIME_TO_SOUND[$k]}
    fi
done

# if not %3 %5 nor %7 then just return the input
if [[ ${#res} -eq 0 ]]
then
    res="$input"
fi

echo "$res"
exit