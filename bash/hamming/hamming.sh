#!/usr/bin/env bash

# Documentation
if [[ "$#" == 0 ]]
then
    echo "Usage: hamming.sh <string1> <string2>"
    exit 1
fi

# Arguments name that match the documentation :)
string1=$1
string2=$2

# Validation
if [[ ${#string1} != ${#string2} ]]
then
    echo "left and right strands must be of equal length"
    exit 1
fi

# Action
diff=0

for (( i=0 ; i < ${#string1} ; i++ ))
do
    if [[ ${string1:$i:1} != ${string2:$i:1} ]]
    then
        diff=$((diff +1))
    fi
done

echo $diff
exit 0
