
def fib(n):
    n1 = 0
    n2 = 1
    if n == 1:
        return n1
    elif n ==2:
        return n2
    else:
        for i in range(2, n): #We start from 2 because we already have 1 and 2 (n1 and n2)
            num = n1 + n2   #Never write a return inside a loop!!
            n1 = n2
            n2 = num
        return num  #It wont work because we need to consider the 1st two numbers, thats why we need the if's

print("5th Fibonnaci's term:", fib(5))
print("11th Fibonnaci's term:", fib(11))
print("55th Fibonnaci's term:", fib(55))