const EARTH_YEAR = 31_557_600; // seconds
const ORBIT_RATIOS = {
  'mercury': 0.240_846_7,
  'venus': 0.615_197_26,
  'earth': 1.0,
  'mars': 1.880_815_8,
  'jupiter': 11.862_615,
  'saturn': 29.447_498,
  'uranus': 84.016_846,
  'neptune': 164.791_32,
};

type Planet = keyof typeof ORBIT_RATIOS;

export function age(planet: Planet, seconds: number): number {
  return Number(
    (
      seconds / (EARTH_YEAR * ORBIT_RATIOS[planet])
    ).toFixed(2)
  );
}
