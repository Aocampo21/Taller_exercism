
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Error")
    else:
        return sum(i != j for i, j in zip(strand_a, strand_b))
