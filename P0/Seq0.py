def seq_ping(): #Ex1
    print("Ok")

def valid_filename():  #Ex2
    from pathlib import Path
    FOLDER = "./sequences/"
    exit = False
    while not exit:
        filename = input("What file do you want to open?:")
        try:
            f = Path(FOLDER + filename + ".txt").read_text()
            exit = True
            return filename
        except FileNotFoundError:
            print("File does not exist. Provide another file")

def seq_read_fasta(FILENAME): #Ex2
    from pathlib import Path
    FOLDER = "./sequences/"
    seq = Path(FOLDER + FILENAME + ".txt").read_text()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_len(FILENAME): #Ex3
    return len(FILENAME)

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
    d = {"A": 0, "C": 0, "T": 0, "G": 0}
    for l in FILENAME:
        d[l] += 1
    return d

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
    FILENAME = "U5"
    sequence = seq_read_fasta(FILENAME)
    seq = sequence[0:20]
    d_complements = {"A": "T", "C": "G", "T": "A", "G": "C"}
    return "".join([d_complements[i] for i in seq])

def seq_frequent_base(FILENAME):  #Ex8
    d = {"A": 0, "C": 0, "T": 0, "G": 0}
    frequent_base = ""
    for l in FILENAME:
        d[l] += 1
        for m in d.keys():
            if d[m] == max(d.values()):
                frequent_base += m + " "
        return frequent_base
