from Seq1 import Seq
print("-----| Practice 1, Exercise 4 |------")
# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("ERROR")

print(f"Sequence 1: (Length:",str(s1.len())+")", (s1))
print(f"Sequence 2: (Length:",str(s2.len())+")", (s2))
print(f"Sequence 3: (Length:",str(s3.len())+")", (s3))