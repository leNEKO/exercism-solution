const COLORS = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white",
] as const;

type Color = typeof COLORS[number];

export function decodedResistorValue([colorA, colorB, colorC]: Color[]): string {
  let value: number = (
      COLORS.indexOf(colorA) * 10
      + COLORS.indexOf(colorB)
    )
    * 10 ** COLORS.indexOf(colorC)
  ;

  let suffix: string = "ohms";

  if (value > 1_000) {
    value *= .001;
    suffix = 'kiloohms';
  }

  return `${value} ${suffix}`;
}
