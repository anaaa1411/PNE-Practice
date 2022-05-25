class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases  #We are assining the string directlly to the atribute
        if strbases == "NULL":
            print("NULL Seq created")
        elif not Seq.valid_sequence(self):
            print("INVALID Seq!")
        else:
            print("New sequence created!")

    @staticmethod  #Now the sequence isn't purple anymore
    def valid_sequence2(sequence):   #(sequence) Is purple because is a method as a previous one
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self): #Ex4
        """Calculate the length of the sequence"""
        if Seq.valid_sequence(self):
            return len(self.strbases)
        else:
            return 0

    def count_base(self): #Ex5
        counts_list = []
        if Seq.valid_sequence(self):
            countA = self.strbases.count("A")
            countC = self.strbases.count("C")
            countT = self.strbases.count("T")
            countG = self.strbases.count("G")
            counts_list.append(countA)
            counts_list.append(countC)
            counts_list.append(countT)
            counts_list.append(countG)
            return counts_list
        else:
            countA = 0
            countC = 0
            countT = 0
            countG = 0
            counts_list.append(countA)
            counts_list.append(countC)
            counts_list.append(countT)
            counts_list.append(countG)
            return counts_list

    def count(self): #Ex6
        if Seq.valid_sequence(self):
            countA = self.strbases.count("A")
            countC = self.strbases.count("C")
            countT = self.strbases.count("T")
            countG = self.strbases.count("G")
            d = {"A": countA, "C": countC, "T": countT, "G": countG}
            return d
        else:
            countA = 0
            countC = 0
            countT = 0
            countG = 0
            d = {"A": countA, "C": countC, "T": countT, "G": countG}
            return d

    def reverse(self): #Ex7
        if self.strbases == "NULL":
            seq_rev = self.strbases
            return seq_rev
        elif not Seq.valid_sequence(self):
            seq_rev = self.strbases
            return seq_rev
        else:
            seq_rev = self.strbases[::-1]
            return seq_rev

    def complement(self): #Ex8
        if self.strbases == "NULL":
            seq_comp = self.strbases
            return seq_comp
        elif not Seq.valid_sequence(self):
            seq_comp = self.strbases
            return seq_comp
        else:
            d_complements = {"A": "T", "C": "G", "T": "A", "G": "C"}
            return "".join([d_complements[i] for i in self.strbases])

    def seq_read_fasta(self, filename): #Ex 9
        f = open(filename, "r").read()
        self.strbases = f[f.find("\n") + 1:].replace("\n", "")
        return self.strbases

    def seq_frequent_base(self):  # Ex8
        d = {"A": 0, "C": 0, "T": 0, "G": 0}
        FILENAME = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
        frequent_base = ""
        for l in self.strbases:
            d[l] += 1
        for m in d.keys():
            if d[m] == max(d.values()):
                frequent_base += m + " "
        return frequent_base

    def mult_bases(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return f"We could not multiply the bases since the sequence is not correct"
        else:
            values = {"A": 2, "C": -1, "G": 3, "T": 5}
            result = 1
            for base in self.strbases:
                for key, val in values.items():
                    if base == key:
                        result = result * values[key]

        return result





    

