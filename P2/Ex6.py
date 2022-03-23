from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 6500
PORT2 = 6501

FILENAME = "FRAT1"
filename = "./sequences/"

s = Seq()
s.seq_read_fasta(filename + FILENAME + ".txt")

# -- Create a client object
c = Client(IP, PORT)
c2 = Client(IP, PORT2)


print(f"Gene FRAT1: {str(s)}")
response = (c.talk(f"Sending {FILENAME} Gene to the server, in fragments of 10 bases..."), c2.talk(f"Sending {FILENAME} Gene to the server, in fragments of 10 bases..."))

i = 0
count = 0
while i < len(s.strbases) and count < 10:
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    if count % 2 == 0:
        print("Fragment", count, ":", fragment)
        response = c2.talk(f"Fragment {count}: {fragment}")
    else:
        print("Fragment", count, ":", fragment)
        response = c.talk(f"Fragment {count}: {fragment}")

