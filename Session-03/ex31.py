def count_bases(seq):   #We dont need the same names inside the functions than in the arguments
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:   #We dont need no ifs
        d[b] += 1
    return d

with open("sequences.txt", "r") as f:
    sequences = f.readlines()
    for seq in sequences:
        new_seq = seq.replace("\n", "")
        print("Total length:", len(new_seq))
        for k, v in count_bases(new_seq).items():
            print(k + ":", v)
