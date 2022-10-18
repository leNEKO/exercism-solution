class Dice {
  readonly faces: number;

  constructor(faces: number) {
    this.faces = faces;
  }

  public roll(): number {
    return (
      Math.round(
        Math.random() * (this.faces - 1)
      ) + 1
    );
  }
}

export class DnDCharacter {
  readonly strength: number = DnDCharacter.generateAbilityScore();
  readonly dexterity: number = DnDCharacter.generateAbilityScore();
  readonly constitution: number = DnDCharacter.generateAbilityScore();
  readonly intelligence: number = DnDCharacter.generateAbilityScore();
  readonly wisdom: number = DnDCharacter.generateAbilityScore();
  readonly charisma: number = DnDCharacter.generateAbilityScore();

  readonly hitpoints: number = 10 + DnDCharacter.getModifierFor(this.constitution);

  public static generateAbilityScore(): number {
    const qty: number = 4;
    const best: number = 3;

    const dices: Dice[] = [...Array(qty)].map(
      () => new Dice(6)
    );

    const rolls: number[] = dices
      .map((dice: Dice): number => dice.roll());

    return rolls.sort().reverse().slice(0, best).reduce(
      (previousValue, currentValue) => previousValue + currentValue
    );
  }

  public static getModifierFor(abilityValue: number): number {
    return Math.floor((abilityValue - 10) / 2)
  }
}
