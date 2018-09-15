#!/usr/bin/env bash

ABC="abcdefghijklmnopqrstuvwxyz" # 26 char latin alphabet

# action
func=$1

# normalizing
input=${2,,} # lowercase string input
alpha=${input//[![:alnum:]]/} # alpha numerical only chars

# common logic
function codec(){
    # loop over each char
    for (( i=0 ; i < ${#alpha} ; i++ )) ; do
        in_char=${alpha:i:1} # input char
        
        left=${ABC%%$in_char*} # input char ABC left substring
        (( k = ${#left} ))  # ABC index
        (( rk = 25 - k)) # ZYX index
        
        if (( k < 26 )); then
            out_char=${ABC:rk:1} # a proper alpha char
        else
            (( out_char = in_char )) # a digit
        fi
        
        echo -n $out_char # output char
    done
}

# specific logic
function encode(){
    str=$(codec $input)
    # split in chunk
    out=""
    for (( i = 0 ; i < ${#str} ; i += 5 )); do
        out="$out ${str:i:5}"
    done
    echo $out
}

function decode(){
    # nothing else special to do
    echo $(codec $input)
}

# feed the input to the proper function
$func input
