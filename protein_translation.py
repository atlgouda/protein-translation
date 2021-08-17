protein_list = {
    "Methionine": ["AUG"],
    "Phenylalanine": ["UUU", "UUC"],
    "Leucine": ["UUA", "UUG"],
    "Serine": ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine": ["UAU", "UAC"],
    "Cysteine": ["UGU", "UGC"],
    "Tryptophan": ["UGG"],
}
stop_codons = ["UAA", "UAG", "UGA"]
valid_codons = [val for codons in protein_list.values() for val in codons]

def proteins(strand):
    # proteins_given should be named "codons_given" upon review
    proteins_given = [strand[i:i+3] for i in range(0, len(strand), 3)]
    strand_proteins = []
    if len(strand) % 3 != 0:
        raise Exception(
            "Incorrect number of characters given, must be divisible by 3")
    for x in proteins_given:
        if x in stop_codons:
            break
        elif x not in valid_codons:
            raise Exception("Invalid codon provided")
        for key, value in protein_list.items():
            if x in value:
                strand_proteins.append(key)
    return strand_proteins

