import Seq0
FILENAME = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]

print("-----| Exercise 3 |------")
for l in FILENAME:
    seq = Seq0.seq_read_fasta(l)
    print("Gene", l, "---> Length:", Seq0.seq_len(seq))
