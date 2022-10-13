import random
import matplotlib.pyplot as plt

def generate_dna(tablenum):

    random.seed(tablenum)

    dna = ['A','C','G','T']

    seq = "".join(random.choices(dna, k=300))

    # replace start with a start codon
    seq = "TAC" + seq[3:]

    # replace any premature stop codons with non-stops
    seq = seq.replace("ATT", "CAG")
    seq = seq.replace("ATC", "GGA")
    seq = seq.replace("ACT", "AAA")

    # Add in a stop codon somewhere towards the end
    stops = ["ATT", "ATC", "ACT"]
    rand_end = 3 * (random.randint(250,300)//3)
    seq = seq[0:rand_end] + random.choice(stops) + seq[rand_end+3:]

    return seq

aa = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "STOP", "UAG": "STOP",
    "UGU": "Cys", "UGC": "Cys", "UGA": "STOP", "UGG": "Trp",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}

DNA = generate_dna(0)
print(DNA)
RNA = "U".join(DNA.split("A"))
RNA = "X".join(RNA.split("C"))
RNA = "C".join(RNA.split("G"))
RNA = "A".join(RNA.split("T"))
RNA = "G".join(RNA.split("X"))
print(RNA)

amino_acids = []
RNA_list = []

for i in range(3, 301, 3):
    RNA_list.append(RNA[i-3:i])

print(amino_acids)
for i, item in enumerate(RNA_list):
    if item in aa:
        if aa[item] == "STOP":
            break
        else:
            amino_acids.append(aa[item])
print("-".join(amino_acids))

plt.hist(amino_acids, bins = len(set(amino_acids)), rwidth=0.8)
plt.show()