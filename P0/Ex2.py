import Seq0

FILENAME = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(FILENAME)
print(sequence[0:20])