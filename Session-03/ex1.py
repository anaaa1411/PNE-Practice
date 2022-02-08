N = 11

n1 = 0
n2 = 1
print(n1, end=" ")
print(n2, end=" ")
for i in range(2, N): #We start from 2 because we already have 1 and 2 (n1 and n2)
    num = n1 + n2
    print(num, end=" ")
    n1 = n2
    n2 = num
print() #This is for adding an end on line character when running the program in the terminal (with: python ex1.py)