<?php

require_once "difference-of-squares.php";

class SquaresTest extends PHPUnit\Framework\TestCase
{
    public function testSquareOfSumsTo5()
    {
        $this->assertEquals(225, squareOfSums(5));
    }

    public function testSumOfSquaresTo5()
    {
        // //$this->markTestSkipped();
        $this->assertEquals(55, sumOfSquares(5));
    }

    public function testDifferenceOfSumsTo5()
    {
        //$this->markTestSkipped();
        $this->assertEquals(170, difference(5));
    }

    public function testSquareOfSumsTo10()
    {
        //$this->markTestSkipped();
        $this->assertEquals(3025, squareOfSums(10));
    }

    public function testSumOfSquaresTo10()
    {
        //$this->markTestSkipped();
        $this->assertEquals(385, sumOfSquares(10));
    }

    public function testDifferenceOfSumsTo10()
    {
        //$this->markTestSkipped();
        $this->assertEquals(2640, difference(10));
    }

    public function testSquareOfSumsTo100()
    {
        //$this->markTestSkipped();
        $this->assertEquals(25502500, squareOfSums(100));
    }

    public function testSumOfSquaresTo100()
    {
        //$this->markTestSkipped();
        $this->assertEquals(338350, sumOfSquares(100));
    }

    public function testDifferenceOfSumsTo100()
    {
        //$this->markTestSkipped();
        $this->assertEquals(25164150, difference(100));
    }
}
