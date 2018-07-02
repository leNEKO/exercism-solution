<?php
// The tests need such a specific implementation
// that i predict others solutions will probably only differs in some variable names
class Allergies
{
    private $score;

    public function __construct(int $score)
    {
        $this->score = $score;
    }

    public function getScore()
    {
        return $this->score;
    }

    public function isAllergicTo(Allergen $allergen)
    {
        $a_score = $allergen->getScore();
        return ($this->score & $a_score) == $a_score;
    }

    public function getList()
    {
        $list = [];
        foreach (Allergen::allergenList() as $allergen) {
            if ($this->isAllergicTo($allergen)) {
                $list[] = $allergen;
            }
        }
        return $list;
    }
}

class Allergen
{
    const EGGS = 1;
    const PEANUTS = 2;
    const SHELLFISH = 4;
    const STRAWBERRIES = 8;
    const TOMATOES = 16;
    const CHOCOLATE = 32;
    const POLLEN = 64;
    const CATS = 128;

    private $score;

    public function __construct($what)
    {
        $this->score = $what;
    }

    public static function allergenList()
    {
        return [
            new Allergen(Allergen::CATS),
            new Allergen(Allergen::CHOCOLATE),
            new Allergen(Allergen::EGGS),
            new Allergen(Allergen::POLLEN),
            new Allergen(Allergen::SHELLFISH),
            new Allergen(Allergen::STRAWBERRIES),
            new Allergen(Allergen::PEANUTS),
            new Allergen(Allergen::TOMATOES),
        ];
    }

    public function getScore()
    {
        return $this->score;
    }

}

if (!debug_backtrace()) {
    $a = new Allergies(3);
    var_dump($a);
    $b = $a->getList();
    var_dump($b);
}
