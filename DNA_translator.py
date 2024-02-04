import pandas as pd

codons =["UUU", "UUC", "UUA", "UUG", "CUU", "CUC", "CUA", "CUG",
"AUU", "AUC", "AUA", "AUG", "GUU", "GUC", "GUA", "GUG", "UCU", "UCC", "UCA",
"UCG", "CCU", "CCC", "CCA", "CCG", "ACU", "ACC", "ACA", "ACG", "GCU",
"GCC", "GCA", "GCG", "UAU", "UAC", "CAU", "CAC", "CAA", "CAG",
"AAU", "AAC", "AAA", "AAG", "GAU", "GAC", "GAA", "GAG",
"UGU", "UGC", "UGG", "CGU", "CGC", "CGA", "CGG", "AGU",
"AGC", "AGA", "AGG", "GGU", "GGC", "GGA", "GGG", "UAA", "UGA", "UAG"]

proteins =["Phenylalanine", "Phenylalanine", "Leucine", "Leucine", "Leucine",
"Leucine", "Leucine", "Leucine", "Isoleucine", "Isoleucine", "Isoleucine",
"Methionine", "Valine", "Valine", "Valine", "Valine", "Serine", "Serine",
"Serine", "Serine", "Proline", "Proline", "Proline", "Proline",
"Threonine", "Threonine", "Threonine", "Threonine", "Alanine", "Alanine",
"Alanine", "Alanine", "Tyrosine", "Tyrosine", "Histidine", "Histidine", "Glutamine",
"Glutamine", "Asparagine", "Asparagine", "Lysine", "Lysine", "Aspartic Acid",
"Aspartic Acid", "Glutamic Acid", "Glutamic Acid", "Cysteine", "Cysteine", "Tryptophan",
"Arginine", "Arginine", "Arginine", "Arginine", "Serine", "Serine", "Arginine", "Arginine",
"Glycine", "Glycine", "Glycine", "Glycine", "", "", ""]

data = pd.DataFrame()
data['codons'] = codons
data['proteins'] = proteins

print("Write a RNA sequence:")
code = input()
index = code.find('AUG')

ii = code.find("UAA" or "UGA" or "UAG")

k = index
result = []

print(code[k:ii-2])

while (k <= len(code) - 3):
    codon = code[k:k+3]
    k += 3
    i = data.query(f"codons == '{codon}'").index[0]
    result.append(data["proteins"][i])
    if (codon == "UAA" or codon == "UGA" or codon == "UAG"):
        break

for codon in result:
    print(codon)