<?php
/*
Mathematically clever solution thanks to http://exercism.io/submissions/53fd3e0ec7e64a58ac9e8671455e5e25
https://math.stackexchange.com/questions/2260/proof-for-formula-for-sum-of-sequence-123-ldotsn
https://www.youtube.com/watch?v=drguFeiCMZw
*/
function squareOfSums(int $n){
    // ((N * (N + 1))/2 ) ^ 2
    return (($n * ($n + 1)) / 2) ** 2;
}

function sumOfSquares(int $n){
    // (N * (N + 1) * (2N + 1)) / 6
    return ($n * ($n +1) * ($n * 2 + 1)) / 6;
}

function difference(int $n){
    return squareOfSums($n) - sumOfSquares($n);
}
