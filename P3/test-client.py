from Client0 import Client

PORT = 6123
IP = "127.0.0.1"

c = Client(IP, PORT)
print(f"Connection to SERVER at {IP}, PORT: {PORT}")

print(" * Testing PING...")
msg = c.talk("PING")
print(msg)

print("* Testing GET...")
msg = c.talk("GET 0")
print("GET 0:", msg)
msg = c.talk("GET 1")
print("GET 1:", msg)
msg = c.talk("GET 2")
print("GET 2:", msg)
msg = c.talk("GET 3")
print("GET 3:", msg)
msg = c.talk("GET 4")
print("GET 4:", msg)

print("\n* Testing INFO...")
msg = c.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(msg)

print("* Testing COMP...")
print("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
msg = c.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(msg)

print("\n* Testing REV...")
print("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
msg = c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(msg)

print("\n* Testing GENE...")

print("GENE U5")
msg = c.talk("GENE U5")
print(msg)

print("\nGENE ADA")
msg = c.talk("GENE ADA")
print(msg)

print("\nGENE FRAT1")
msg = c.talk("GENE FRAT1")
print(msg)

print("\nGENE FXN")
msg = c.talk("GENE FXN")
print(msg)

print("\nGENE RNU6_269P")
msg = c.talk("GENE RNU6_269P")
print(msg)

