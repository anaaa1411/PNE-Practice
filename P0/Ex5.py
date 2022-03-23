import Seq0

FILENAME = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
FOLDER = "./sequences/"
print("-----| Exercise 5 |------")

for l in FILENAME:
    seq = Seq0.seq_read_fasta(FOLDER, l)
    print("Gene", l, ":", Seq0.seq_count(seq))
