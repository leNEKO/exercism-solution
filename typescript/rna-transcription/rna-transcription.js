const DnaRnaMap = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
};
export function toRna(dnaSequence) {
    return dnaSequence.split('').map((v) => (DnaRnaMap[v])).join('');
}
