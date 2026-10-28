import sys


codon_table = {
    "UUU": ("F", 0),
    "UUC": ("F", 0),
    "UUA": ("L", 0),
    "UUG": ("L", 1),
    
    "UCU": ("S", 0),
    "UCC": ("S", 0),
    "UCA": ("S", 0),
    "UCG": ("S", 0),

    "UAU": ("Y", 0),
    "UAC": ("Y", 0),
    "UAA": ("*", 2),
    "UAG": ("*", 2),

    "UGU": ("C", 0),
    "UGC": ("C", 0),
    "UGA": ("*", 2),
    "UGG": ("W", 0),

    # ----------------

    "CUU": ("L", 0),
    "CUC": ("L", 0),
    "CUA": ("L", 0),
    "CUG": ("L", 1),
    
    "CCU": ("P", 0),
    "CCC": ("P", 0),
    "CCA": ("P", 0),
    "CCG": ("P", 0),

    "CAU": ("H", 0),
    "CAC": ("H", 0),
    "CAA": ("Q", 0),
    "CAG": ("Q", 0),

    "CGU": ("R", 0),
    "CGC": ("R", 0),
    "CGA": ("R", 0),
    "CGG": ("R", 0),

    # -------------------

    "AUU": ("I", 0),
    "AUC": ("I", 0),
    "AUA": ("I", 0),
    "AUG": ("M", 1),
    
    "ACU": ("T", 0),
    "ACC": ("T", 0),
    "ACA": ("T", 0),
    "ACG": ("T", 0),

    "AAU": ("N", 0),
    "AAC": ("N", 0),
    "AAA": ("K", 0),
    "AAG": ("K", 0),

    "AGU": ("S", 0),
    "AGC": ("S", 0),
    "AGA": ("R", 0),
    "AGG": ("R", 0),

    # ------------------

    "GUU": ("V", 0),
    "GUC": ("V", 0),
    "GUA": ("V", 0),
    "GUG": ("V", 0),
    
    "GCU": ("A", 0),
    "GCC": ("A", 0),
    "GCA": ("A", 0),
    "GCG": ("A", 0),

    "GAU": ("D", 0),
    "GAC": ("D", 0),
    "GAA": ("E", 2),
    "GAG": ("E", 0),

    "GGU": ("G", 0),
    "GGC": ("G", 0),
    "GGA": ("G", 0),
    "GGG": ("G", 0),

}



def readDNA(filename: str):
    # open file
    # check to see if file is valid
    # create string of dna
    dna = ""
    file = open(filename, 'r')

    for line in file:
        line = line.strip()
        # skip line if empty
        if line == "":
            continue

    file.close()
    return dna

def ConvertDNAtoRNA(DNA: str) -> str:
    # Convert every T to a U
    return DNA.upper().replace("T", "U")

def valid(a: str) -> bool:
    return a == "U" or a == "C" or a == "A" or a == "G"

def main():
    # Bring up codon lookup table

    # Using input table, read in DNA string
    DNA = readDNA(sys.argv[1])
    # convert dna string to rna

    RNA = ConvertDNAtoRNA(DNA)

    codon_list = []

    # convert to codon
    for i in range(0, len(RNA), 3):
        A, B, C = RNA[i], RNA[i + 1], RNA[i + 2]
        if not valid(A) or not valid(B) or not valid(C):
            print("Invalid DNA strand")
            sys.exit(1)
        # look up substring in codon table
        seq = "".join([A, B, C])
        codon, code = codon_table[seq]
        # if code is 0, do nothing
        # if code is 1, then it's a starting codon
        # if code is 2, then it's a stop codon
        if code == 1 and len(codon_list) > 0:
            # failure in codon, abort
            print("Error: Misplaced starting codon")
            sys.exit(1)
        else:
            codon_list.append(codon)

        if code == 2:
            break

    # Join together list and output as string
    # Write string to file
    codon_filename = sys.argv[1] + "_codons"
    with open(codon_filename, "w", encoding="utf-8") as file:
        file.write("".join(codon_list))
        file.close()

    sys.exit(0)


if __name__ == "__main__":
    main()