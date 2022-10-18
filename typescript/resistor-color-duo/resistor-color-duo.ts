enum Colors {
  black = 0,
  brown = 1,
  red = 2,
  orange = 3,
  yellow = 4,
  green = 5,
  blue = 6,
  violet = 7,
  grey = 8,
  white = 9,
}

export function decodedValue(values: Array<string>): number {
  const colors: Array<Colors> = values
    .map<number>(
      (v) => (<any>Colors)[v]
    )
  ;

  return Number.parseInt(
    `${colors[0]}${colors[1]}`,
    10
  );
}
