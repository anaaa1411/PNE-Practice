from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 7500

FILENAME = ["U5", "FRAT1", "ADA"]
filename = "./sequences/"
for l in FILENAME:
    s = Seq()
    s.seq_read_fasta(filename + l + ".txt")

    # -- Create a client object
    c = Client(IP, PORT)

    print(f"To Server: Sending {l} to the server...")
    response = c.talk(f"Sending {l} to the server...")
    print(f"From Server: {response}")

    print(f"To Server: {str(s)}")
    response = c.talk(str(s))
    print(f"From Server: {response}")
