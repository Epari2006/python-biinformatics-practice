def gc_content(seq):
    """Return GC content percentage of a DNA sequence."""
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100


def transcription(seq):
    """Convert DNA sequence to RNA sequence."""
    return seq.replace("T", "U")


def complement(seq):
    """Return the complementary DNA sequence."""
    return seq.translate(str.maketrans("ATGC", "TACG"))


def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    return complement(seq)[::-1]


def dna_length(seq):
    """Return the length of a DNA sequence."""
    return len(seq)


if __name__ == "__main__":
    dna_seq = "ATGCGATCGATCG"

    print("DNA Sequence:", dna_seq)
    print("Length:", dna_length(dna_seq))
    print("GC Content:", round(gc_content(dna_seq), 2), "%")
    print("RNA Transcript:", transcription(dna_seq))
    print("Complement:", complement(dna_seq))
    print("Reverse Complement:", reverse_complement(dna_seq))
