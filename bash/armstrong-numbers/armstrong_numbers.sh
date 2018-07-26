#!/usr/bin/env bash

input="$@"

len=${#input} # numbers of digits
sum=0 # init sum

# loop over each digit
for (( i=0 ; i<$len ; i++ ))
do
    c=${input:$i:1}
    sum=$(echo "$sum+($c^$len)" | bc)
done

if [[ $sum -eq $input ]]
then
    echo "true"
    exit 0
fi

echo "false"
exit 1