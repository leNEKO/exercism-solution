#!/usr/bin/env bash

# in tests for alternate whitespaces
# new lines \n \r and tabs \t are not properly escaped
# they are passed as "\n\r\t"
# instead of $'\n\r\t'
str=$(echo $1 | sed 's/\\\w//g')
chars=$(echo $str | tr -cd '[:alnum:][:punct:]')
alpha=$(echo $str | tr -cd '[:alpha:]')

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