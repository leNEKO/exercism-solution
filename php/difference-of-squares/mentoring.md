# Suggestions

## Further "map / filter / reduce" approach

> trying the reduce method

If you want to go further with this "map, filter, reduce" approach, you can try to implement the sumOfSquares with a simple `array_reduce()` instead of the nested `array_sum(array_map(…))` combo.

## Using the math alternative

> information about the boring math way

Alternatively, there is math formulas to calculate these:

- Sum of squares `(N * (N + 1) * (2N + 1)) / 6`
- Square of sums `((N * (N + 1)) /2 ) ^ 2`

## Exponentiation

> using `x ** 2` instead of `pow(x, 2)` or `x * x`

Another trick, you can write `pow($i, 2)` with the exponentiation operator `$i ** 2`.
