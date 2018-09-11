    <?php

class Series
{
    public $seq;

    public function __construct(string $seq)
    {
        if ($seq != preg_replace("/\D/", "", $seq)) { // …
            throw new InvalidArgumentException();
        }
        $this->seq = $seq;
    }

    public function largestProduct(int $length)
    {
        $seq_length = strlen($this->seq);

        if ($length > $seq_length) {
            throw new InvalidArgumentException();
        }

        if (!$seq_length || !$length) {
            return 1; // why … i don't know, explication are more confusing to me … whatever here 1
        }

        if ($length < 0) {
            throw new InvalidArgumentException("must be >= 0");
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
