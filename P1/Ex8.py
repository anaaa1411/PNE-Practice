from Seq1 import Seq
print("-----| Practice 1, Exercise 8 |------")
# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("ERROR")

print(f"Sequence 1: (Length:",str(s1.len())+")", (s1))
print(f"\tBases:", s1.count())
print(f"\tRev:", s1.reverse())
print(f"\tComp:", s1.complement())
print(f"Sequence 2: (Length:",str(s2.len())+")", (s2))
print(f"\tBases:", s2.count())
print(f"\tRev:", s2.reverse())
print(f"\tComp:", s2.complement())
print(f"Sequence 3: (Length:",str(s3.len())+")", (s3))
print(f"\tBases:", s3.count())
print(f"\tRev:", s3.reverse())
print(f"\tComp:", s3.complement())