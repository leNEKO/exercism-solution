#!/usr/bin/env bash

# remove diacritics, don't think it is possible bash only
str=$(echo $1 | iconv -t utf8 -t ascii//translit)

# check if each ascii char is in the lower sentence
for c in {a..z}; do
    if [[ ${str,,} =~ "$c" ]]; then
        (( alpha_count++ ))
    fi
done

# check if pangram
(( alpha_count == 26 )) && echo "true" || echo "false"
