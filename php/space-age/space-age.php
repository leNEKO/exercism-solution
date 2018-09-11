<?php
class SpaceAge
{
    private const EARTH_YEAR = 31557600;
    private const RATIOS = [
        "earth" => 1,
        "mercury" => 0.2408467,
        "venus" => 0.61519726,
        "mars" => 1.8808158,
        "jupiter" => 11.862615,
        "saturn" => 29.447498,
        "uranus" => 84.016846,
        "neptune" => 164.79132,
    ];

    public function __call($func, $params)
    {
        if (in_array($func, array_keys(self::RATIOS))) {
            $years = $this->seconds / (self::EARTH_YEAR * self::RATIOS[$func]);
            return round($years, 2);
        }
    }

    public function __construct(int $seconds)
    {
        $this->seconds = $seconds;
    }

    public function seconds()
    {
        return $this->seconds;
    }
}
