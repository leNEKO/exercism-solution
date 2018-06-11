def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Not same strand lengths")

    distance = sum(1 for val_a, val_b in zip(
        strand_a, strand_b) if val_a != val_b)

    return distance
