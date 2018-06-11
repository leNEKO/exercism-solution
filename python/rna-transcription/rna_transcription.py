def to_rna(dna_strand):
    map = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    rna_strand = []
    for char in dna_strand:
        try:
            rna_strand.append(map[char])
        except:
            raise Exception("Extradimensionnal life detected")
    return "".join(rna_strand)
