from Seq1 import Seq
filename = "./sequences/U5.txt"
print("-----| Practice 1, Exercise 9 |------")

# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.seq_read_fasta(filename)

print(f"Sequence: (Length:",str(s.len())+")", (s))
print(f"\tBases:", s.count())
print(f"\tRev:", s.reverse())
print(f"\tComp:", s.complement())