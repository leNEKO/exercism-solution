#!/usr/bin/env bash

str="${1//\\[a-z]/}" # hack removing fake unescaped whitespaces
chars="${str//[![:alnum:][:punct:]]/}"
alpha="${str//[![:alpha:]]/}"

if [[ "$chars" == "" ]]; then
    echo "Fine. Be that way!"
    exit 0
fi

# sentence properties
[ "${chars: -1}" == "?" ] && is_question=true
[ "${alpha^^}" == "$alpha" ] && [ "$alpha" != "" ] && is_upper=true

r="Whatever."
if [[ $is_question && $is_upper ]];then
    r="Calm down, I know what I'm doing!"
    
    elif [[ $is_upper ]]; then
    r="Whoa, chill out!"
    
    elif [[ $is_question ]]; then
    r="Sure."
fi

echo $r
exit 0