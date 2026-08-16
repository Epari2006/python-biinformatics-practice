

def gc_content(seq):
    """Return GC content percentage of a DNA sequence."""
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100

def transcription(seq):
    """Convert DNA sequence to RNA sequence."""
    return seq.replace("T", "U")

# Example usage
if __name__ == "__main__":
    dna_seq = "ATGCGTAC"
    print("DNA Sequence:", dna_seq)
    print("GC Content (%):", round(gc_content(dna_seq), 2))
    print("RNA Transcript:", transcription(dna_seq))
