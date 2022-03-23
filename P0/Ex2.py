import Seq0
FOLDER = "./sequences/"
FILENAME = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(FOLDER ,FILENAME)
print(sequence[0:20])