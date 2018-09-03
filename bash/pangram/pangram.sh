#!/usr/bin/env bash

# count distinct alphas
alpha_count=$(echo $1 |
    iconv -t utf8 -t ascii//TRANSLIT | # convert to ASCII
    tr -cd '[[:alpha:]]' | # alpha only
    tr A-Z a-z | # to lower case
    fold -w1 | # split to line
    sort -u | # remove duplicate
    wc -l # count lines
)

# check if pangram
([ $alpha_count == 26 ]) && echo "true" || echo "false"
