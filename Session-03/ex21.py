
def count_bases(seq):   #We dont need the same names inside the functions than in the arguments
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:   #We dont need no ifs
        d[b] += 1
    return d

dna_seq = input("Introduce the sequence: ")
print("Total length:", len(dna_seq))
for k,v in count_bases(dna_seq).items():
    print(k + ":", v)