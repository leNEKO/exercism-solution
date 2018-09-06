#!/usr/bin/env bash

# count distinct alphas
alpha_count=$(echo $1 |
    iconv -t utf8 -t ascii//TRANSLIT | # convert to ASCII for handling diacritics and ligatures
    tr -cd '[:alpha:]' | # alpha only
    tr A-Z a-z | # to lower case
    fold -w1 | # split to line
    sort |
    uniq |
    wc -l
)

# check if pangram
([ $alpha_count == 26 ]) && echo "true" || echo "false"
