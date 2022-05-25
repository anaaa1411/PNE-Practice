import socket
from Seq1 import Seq
import termcolor

def count_bases(seq):
    argument = Seq(arg.replace('"', ""))
    base_dict = Seq.count(argument)
    total = sum(base_dict.values())
    for k, v in base_dict.items():
        base_dict[k] = [v, round((v * 100) / total, 1)]
    return base_dict

def convert_message(base_count):
    message = ""
    for k,v in base_count.items():
        message += k + ": " + str(v[0]) + " (" + str(v[1]) + "%)" + "\n"
    return message

def info_operation(arg):
    base_count = count_bases(arg)
    response = "Sequence: " + arg + "\n"
    response += "Total length: " + str(len(arg)) + "\n"
    response += convert_message(base_count)
    return response

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 6123
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("SEQ Server configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()

        # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    else:
        sequences = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA", "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode().replace("\n", "").strip()
        splitted_command = msg.split(" ")
        cmd = splitted_command[0]
        if cmd != "PING":
           arg = splitted_command[1]
           termcolor.cprint(cmd, "green")
        if cmd == "PING": #Ex1
            response = "OK!\n"
            termcolor.cprint("PING command!", "green")
            print(response)
        elif cmd == "GET":  #Ex2
            try:
                index = int(arg)
                response = sequences[index]
                print(response + "\n")
            except ValueError:
                response = "The argument for the GET command must be a number from 0 to 4"
            except IndexError:
                response = "The argument for the GET command must be a number from 0 to 4"
        elif cmd == "INFO":  #Ex3
            try:
                response = info_operation(arg)
                print(response)
            except ZeroDivisionError:
                response = "The argument is wrong. Try entering sequence characters only (A,C,G or T)."
        elif cmd == "COMP":  #Ex4
            sequence = Seq(arg)
            response = sequence.complement()
            print(response + "\n")
        elif cmd == "REV":  #Ex5
            sequence = Seq(arg)
            response = sequence.reverse()
            print(response + "\n")
        elif cmd == "GENE":  #Ex6
            if arg == "U5" or arg == "FRAT1" or arg == "ADA" or arg == "FXN" or arg == "RNU6_269P":
                filename = "./sequences/"
                sequence = Seq()
                response = sequence.seq_read_fasta(filename + arg + ".txt")
                print(response + "\n")
            else:
                response = "Wrong gene. Try: U5, ADA, FRAT1, FXN or RNU6_269P."
        elif cmd == "MULT":  #EXAM
            sequence = Seq(arg)
            response = str(sequence.mult_bases())
            print(response + "\n")

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()