type DnaName = 'G' | 'C' | 'T' | 'A';
type RnaName = 'C' | 'G' | 'A' | 'U';

const DnaRnaMap: Record<DnaName, RnaName> = {
  'G': 'C',
  'C': 'G',
  'T': 'A',
  'A': 'U',
} as const;

export function toRna(dnaSequence: string): string {
  return dnaSequence.split('').map<RnaName>(
    (v) => (
      DnaRnaMap[v]

    )
  ).join('');
}
