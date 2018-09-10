#!/usr/bin/env bash

missing_bc="$(hash bc 2>&1)"
if [[ $missing_bc ]]
then
    echo "Error: how did you get rid of bc ?" >&2
    exit 1
fi

input="$@"
if [[ $input -gt 0 && $input -lt 65 ]]
then
    echo "2^($input-1)" | bc
    exit 0
else
    echo "Error: invalid input" >&2
    exit 1
fi
