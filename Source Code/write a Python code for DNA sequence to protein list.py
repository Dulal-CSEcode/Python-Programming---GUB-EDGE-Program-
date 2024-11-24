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

codon_dict = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
    "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "CCC": "Pro", "CCA": "Pro", "CCG": "Pro", "CAU": "His",
    "CAC": "His", "CAA": "Gln", "CAG": "Gln", "CGU": "Arg",
    "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AUU": "Ile",
    "AUC": "Ile", "AUA": "Ile", "AUG": "Met", "ACU": "Thr",
    "ACC": "Thr", "ACA": "Thr", "ACG": "Thr", "AAU": "Asn",
    "AAC": "Asn", "AAA": "Lys", "AAG": "Lys", "AGU": "Ser",
    "AGC": "Ser", "AGA": "Arg", "AGG": "Arg", "GUU": "Val",
    "GUC": "Val", "GUA": "Val", "GUG": "Val", "GCU": "Ala",
    "GCC": "Ala", "GCA": "Ala", "GCG": "Ala", "GAU": "Asp",
    "GAC": "Asp", "GAA": "Glu", "GAG": "Glu", "GGU": "Gly",
    "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}

if __name__ == "__main__":
    dna_sequence = input("Enter a DNA sequence: ")
    rna_sequence = dna_to_rna(dna_sequence)
    print("RNA sequence:", rna_sequence)

    codons = rna_codons(rna_sequence)
    print("Codons:", codons)

    proteins = []
    for codon in codons:
        amino_acid = codon_dict.get(codon)
        if amino_acid:
            proteins.append(amino_acid)

    print("Proteins created:", proteins)
