#!/usr/bin/env bash

who=$([ "$#" == 0  ] && echo "you" || echo "$1")

echo "One for $who, one for me."