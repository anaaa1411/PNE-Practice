import Seq0

seq1 = "ATTCCCGGGG"

print(f"Seq:    seq1")
print(f"  Rev : {Seq0.seq_reverse()}")
print(f"  Comp: {Seq0.seq_complement(seq1)}")
print(f"  Length: {Seq0.seq_len(seq1)}")
print(f"    A: {Seq0.seq_count_base(seq1, 'A')}")
print(f"    T: {Seq0.seq_count_base(seq1, 'T')}")
print(f"    C: {Seq0.seq_count_base(seq1, 'C')}")
print(f"    G: {Seq0.seq_count_base(seq1, 'G')}")