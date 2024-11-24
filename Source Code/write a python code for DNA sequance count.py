def count_nucleotides(dna_sequence):

    nucleotide_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for nucleotide in dna_sequence.upper():
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1
    return nucleotide_counts


if __name__ == "__main__":
    dna = input("Enter a DNA sequence: ")
    counts = count_nucleotides(dna)
    print("Nucleotide counts:")
    for nucleotide, count in counts.items():
        print(f"{nucleotide}: {count}")