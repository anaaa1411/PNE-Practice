print("Hello, this is my first Pycharm code")
print("Again!!!!")
print("Hello, this is my first Pycharm code")
print("Again!!!!")
print("Hello, this is my first Pycharm code")
print("Again!!!!")
print("Hello, this is my first Pycharm code")
print("Again!!!!")
print("Hello, this is my first Pycharm code")
print("Again!!!!")



countA = 0
        countC = 0
        countT = 0
        countG = 0
        for base in file:
            if base == "A":
                countA += 1
            if base == "C":
                countC += 1
            if base == "T":
                countT += 1
            if base == "G":
                countG += 1
        print("Gene", l, ":")
        print("A:", countA)
        print("C:", countC)
        print("T:", countT)
        print("G:", countG)

import Seq0
FILENAME = ["U5.txt", "FRAT1.txt", "ADA.txt", "FXN.txt", "RNU6_269P.txt"]
base = ["A", "C", "G", "T"]
print(Seq0.seq_count_base(FILENAME, base))




def seq_len(FILENAME): #Ex3
    for l in FILENAME:
        print("Gene", l, "---> Length:",(len(seq_read_fasta(l))))






def seq_count(FILENAME): #Ex5
    for l in FILENAME:
        file = seq_read_fasta(l)
        countA = 0
        countC = 0
        countT = 0
        countG = 0
        for base in file:
            if base == "A":
                countA += 1
            if base == "C":
                countC += 1
            if base == "T":
                countT += 1
            if base == "G":
                countG += 1
        d = {"A":countA, "C":countC, "T":countT, "G":countG}
        print("Gene", l, ":", d)

