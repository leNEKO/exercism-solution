<?php

class Series
{
    public $seq;

    public function __construct(string $seq)
    {
        // seq. must be digits only
        if (preg_match_all("/[^\d]/", $seq, $m)) {
            throw new InvalidArgumentException("Invalid seq.");
        }
        $this->seq = $seq;
    }

    public function largestProduct(int $length): int
    {
        $seq_length = strlen($this->seq);

        // 0 <= length < seq. length
        if ($seq_length < $length || $length < 0) {
            throw new InvalidArgumentException("Invalid length");
        }

        if (!$length) {
            return 1;
        }

        $hi_product = 0;
        $max = $seq_length - $length;

        for ($i = 0; $i <= $max; $i++) {
            $sub = substr($this->seq, $i, $length);
            $product = array_product(str_split($sub));

            if ($product > $hi_product) {
                $hi_product = $product;
            }
        }
        return $hi_product;
    }
}
