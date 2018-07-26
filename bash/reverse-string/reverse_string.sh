#!/usr/bin/env bash

input="$@"

# the simple way that need "rev"
# echo $input | rev

# the bash only way
for(( i=${#input}-1 ; i>=0 ; i-- ))
do
    reversed="$reversed${input:$i:1}"
done

echo $reversed