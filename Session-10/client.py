import socket

# SERVER IP, PORT
PORT = 20500
IP = "127.0.0.1"  #la ip 0.0.0.0 solo esta permitida para los servidores, en el cliente hay que  usar la ip local si esta en la misma maquina que el servidor
c = Client(IP, PORT)
# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #1º se crea un soket nuevo

# establish the connection to the Server (IP, PORT)
#s.connect((IP, PORT))   # 2º Para conectar el socket cliente  y el soket servidor     #Para hacer tu practica, hazlo con el .talk()

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes

print(" * Testing PING")
msg = c.talk("PING")
#s.send(str.encode("PING"))   # 3º Enviamos un mensaje al server
    # Receive data from the server
#msg = s.recv(2048)     # 4º Para recivir un mensaje del servidor
print(msg.decode("utf-8"))  # 5º --> Para imprimir el mensaje del sservidor
#s.close()


print("* Testing GET...")
msg = c.talk("GET  0")
    #Por cada mensaje que enviamos nos tenemos que conectar y cerrar
    #s.connect((IP, PORT))
    #print(" * Testing GET ...")   #Esto se hace a mano siempre, nunca con inputs
    #s.send(str.encode("GET 0"))
    #msg = s.recv(2048)
print("GET 0:", msg.decode("utf-8"))   #Mirar si en el talk estamso decodificando el mensaje. si es así, entonces no hace falta poner decode aqui, solo habria que poner msg
msg = c.talk("GET  1")
print("GET 1:", msg.decode("utf-8"))
msg = c.talk("GET  2")
print("GET 2:", msg.decode("utf-8"))
msg = c.talk("GET  3")
print("GET 3:", msg.decode("utf-8"))
# Closing the socket
#s.close()    # cerramos el socket   #CON LOS .TALK LOS CLOSE NO HACEN FALTA !!!!!!


print("* Testing INFO...")
msg = c.talk("INFO  ACCTGGGGGG")
print(msg)

print("* Testing COMP...")
print("COMP  ACCTGGGGGG")
msg = c.talk("COMP  ACCTGGGGGG")
print(msg)



#Por cada send que hay en el cliente va a haber un recv en el servidor, y por cada mensae en el servidor va a haber un recv en el cliente