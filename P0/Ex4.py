import Seq0
FILENAME = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
base = ["A", "C", "T", "G"]
countsA, countsC, countsT, countsG = Seq0.seq_count_base(FILENAME, base)
print("-----| Exercise 4 |------")
i = -1
for l in FILENAME:
    i += 1
    print("\nGene", l, ":")
    print("\tA:", countsA[i])
    print("\tC:", countsC[i])
    print("\tT:", countsT[i])
    print("\tG:", countsG[i])
