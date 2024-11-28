
def dna_to_rna(dna_sequence):
    """Converts a DNA sequence to an RNA sequence."""
    return dna_sequence.replace('T', 'U')

def rna_codons(rna_sequence):
    """Divides an RNA sequence into codons (groups of 3 nucleotides)."""
    codons = []
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        if len(codon) == 3:  # Only add complete codons
          codons.append(codon)
    return codons

if __name__ == "__main__":
    dna_sequence = input("Enter a DNA sequence: ")
    rna_sequence = dna_to_rna(dna_sequence)
    print("RNA sequence:", rna_sequence)
    codons = rna_codons(rna_sequence)
    print("Codons:", codons)