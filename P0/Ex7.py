import Seq0
FILENAME = "U5"
FOLDER = "./sequences/"
sequence = Seq0.seq_read_fasta(FOLDER, FILENAME)
print("-----| Exercise 7 |------")
print("Gene U5:")
print("Frag:", sequence[0:20])
print("Comp:", Seq0.seq_complement(FILENAME))