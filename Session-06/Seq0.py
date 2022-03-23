def seq_ping(): #Ex1
    print("Ok")

def valid_filename():  #Ex2
    from pathlib import Path
    FOLDER = "../sequences/"
    exit = False
    while not exit:
        filename = input("What file do you want to open?:")
        try:
            f = Path(FOLDER + filename).read_text()
            exit = True
            return filename
        except FileNotFoundError:
            print("File does not exist. Provide another file")

def seq_read_fasta(FILENAME): #Ex2
    from pathlib import Path
    FOLDER = "../sequences/"
    seq = Path(FOLDER + FILENAME).read_text()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_len(FILENAME): #Ex3
    list_length = []
    for l in FILENAME:
        ret_len = len(seq_read_fasta(l))
        list_length.append(ret_len)
    return list_length

def seq_count_base(FILENAME, base): #Ex4
    countsA = []
    countsC = []
    countsT = []
    countsG = []
    for l in FILENAME:
        file = seq_read_fasta(l)
        countA = file.count(base[0])
        countC = file.count(base[1])
        countT = file.count(base[2])
        countG = file.count(base[3])
        countsA.append(countA)
        countsC.append(countC)
        countsT.append(countT)
        countsG.append(countG)
    return countsA, countsC, countsT, countsG

def seq_count(FILENAME): #Ex5
    base = ["A", "C", "T", "G"]
    list_dict = []
    i = -1
    for l in FILENAME:
        i += 1
        countsA, countsC, countsT , countsG = seq_count_base(FILENAME, base)
        d = {"A": countsA[i], "C": countsC[i], "T": countsT[i], "G": countsG[i]}
        list_dict.append(d)
    return list_dict

def seq_reverse(): #Ex6
    from pathlib import Path
    FOLDER = "./sequences/"
    FILENAME = "U5.txt"
    seq = Path(FOLDER + FILENAME).read_text()
    seq = seq[seq.find("\n"):].replace("\n", "")
    seq_frag = seq[0:20]
    seq_rev = seq_frag[::-1]
    return seq_frag, seq_rev

def seq_complement(FILENAME): #Ex7
    FILENAME = "U5.txt"
    sequence = seq_read_fasta(FILENAME)
    seq = sequence[0:20]
    for i in seq:
        if i == "A":
            print("T", end="")
        elif i == "T":
            print("A", end="")
        elif i == "C":
            print("G", end="")
        elif i == "G":
            print("C", end="")

