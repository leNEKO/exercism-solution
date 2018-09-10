#!/usr/bin/env bash

input=$1

digits=${input//[![:digit:]]/}
length=${#digits}

# validate length and symbols
if [[ $length < 2 || ${input//[[:digit:] ]/} ]]; then
    echo "false"
    exit 0
fi

# init sums
odds=0
evens=0
for (( i=0 ; i < length  ; i++ )); do
    pos=$(( length -i -1 )) # right -> left reading
    digit=${digits:pos:1}
    
    if (( i % 2 )); then
        d=$(( digit * 2 )) # double digit
        q=$(( d / 10 )) # quotient
        r=$(( d % 10 )) # remainder
        (( odds += (q+r) ))
    else
        (( evens += digit ))
    fi
done

checksum=$(( (odds + evens) % 10 ))

[[ $checksum == 0 ]] && echo "true" || echo "false"
exit 0