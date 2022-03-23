import Seq0
FOLDER = "./sequences/"
FILENAME = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
print("-----| Exercise 8 |------")
for l in FILENAME:
    seq = Seq0.seq_read_fasta(FOLDER, l)
    print("Gene", l, ": Most frequent Base:", Seq0.seq_frequent_base(seq))



