from Seq1 import Seq
print("-----| Practice 1, Exercise 10 |------")
FILENAME = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
filename = "./sequences/"


for l in FILENAME:
    s = Seq()
    seq = s.seq_read_fasta(filename + l + ".txt")
    print("Gene", l, ": Most frequent Base:", s.seq_frequent_base())
