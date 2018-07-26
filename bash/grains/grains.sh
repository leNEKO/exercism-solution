#!/usr/bin/env bash
input="$@"
if [[ $input -gt 0 && $input -lt 65 ]]
then
    echo "2^($input-1)" | bc
    exit 0
else
    echo "Error: invalid input" >&2
    exit 1
fi
