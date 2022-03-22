from Seq1 import Seq   #If we only put "import Seq1", we would have to put Seq1.whatever when defining s1 and s2

s1 = Seq("ACCTGC")   #It would have been: Seq1.Seq(Act...)
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")