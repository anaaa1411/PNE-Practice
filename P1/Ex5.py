from Seq1 import Seq
print("-----| Practice 1, Exercise 5 |------")
# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("ERROR")

print(f"Sequence 1: (Length:",str(s1.len())+")", (s1))
print(f"\tA:", s1.count_base()[0], "\tC:", s1.count_base()[1],"\tT:" , s1.count_base()[2], "\tG:", s1.count_base()[3])
print(f"Sequence 2: (Length:",str(s2.len())+")", (s2))
print(f"\tA:", s2.count_base()[0], "\tC:", s2.count_base()[1],"\tT:" , s2.count_base()[2], "\tG:", s2.count_base()[3])
print(f"Sequence 3: (Length:",str(s3.len())+")", (s3))
print(f"\tA:", s3.count_base()[0], "\tC:", s3.count_base()[1],"\tT:" , s3.count_base()[2], "\tG:", s3.count_base()[3])