from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 20500

FILENAME = "FRAT1"
filename = "./sequences/"

s = Seq()
s.seq_read_fasta(filename + FILENAME + ".txt")

# -- Create a client object
c = Client(IP, PORT)

print(f"Gene FRAT1: {str(s)}")
response = c.talk(f"Sending {FILENAME} Gene to the server, in fragments of 10 bases...")

i = 0
count = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    print("Fragment", count, ":", fragment)
    response = c.talk(f"Fragment {count}: {fragment}")


