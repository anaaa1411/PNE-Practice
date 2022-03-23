import socket
from Seq1 import Seq

def count_bases(seq):   #NO pongas esto talcual, utiliza lo de otras practicas
    base_dict = Seq.count_base(arg)
    #d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in base_dict:
        base_dict[b] += 1

    total = sum(base_dict.values())
   # p = {"A": 0, "C": 0, "G": 0, "T": 0}
    for k, v in base_dict.items():
        base_dict[k] = [v, (v * 100) / total]
    return base_dict

def convert_message(base_count):
    message = ""  #Como queremos recivir un string, ponemos un str vacio
    for k,v in base_count.items():
        message += k + ": " + str(v[0]) + " (" + str(v[1]) + "%)" + "\n"
    return message

def info_operation(arg):
    base_count = count_bases(arg)
    response = "Sequence: " + arg + "\n"  # Los saltos de linea "\n" son importantes para que nos queden bien  los esapacios que nos piden!!
    response += "Total length: " + str(len(arg)) + "\n"
    response += convert_message(base_count)  # Con el += vamos concatenando los response
    return response

SEQUENCES = ["ACGTACGT", "TGAAAAA", "AAAAAAAA", "CCCCCC", "GGGGGGGG"]

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 20500 #El puerto siempre cambia   #PAra fuera de la universidad : numeros grandes que empiezen por 20 , ej: 20500
IP = "0.0.0.0" #Esta es la ip generica :"127.0.0.1", si el cliente se conecta a este puerto siempre llega (si scon elcliente y la maquina en el mismo sitio)   #Para fuera de la uni : 0.0.0.0

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    (cs, client_ip_port) = ls.accept()    #Para esperar la conexion, cunado la recive

    print("A client has connected to the server!")

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)  #Para recibir el mensaje

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode().replace("\n", "").strip()   #Esto representa el string recivido del cliente #El replace es para cuando escribimos el PING desde la terminal externa  y hay un hueco, para eliminarlo

    split_list = msg.split(" ")   #Para dividir el texto que nos llega, en 2 partes
    cmd = split_list[0]  #El comando va a estar en la posicion 0

    if cmd != "PING":
        arg = split_list[1]   #Si el comando es diferente de PING el argumento siempre va a estar en esa posicion[1] (PING no tiene argumentos)


    # -- Manage message. # COn esto lo unico que tenemos que hacer para gestionar un nuevo comando es añadir un elif con otro cdm.
    if cmd == "PING":
        response = "PING OK!" #Esto se envia al cliente, que imprimara esa respuesta
    elif cmd == "REV":
        response = arg[::-1]
    elif cmd == "INFO":  #Como tiene mas de una linea lo ideal es hacer una funcion
        response = info_operation(arg)
    elif cmd == "COMP":
        sequence = Seq(arg)
        response = sequence.complement()
    elif cmd == "GET":
        try:
            index = int(arg)
            response = SEQUENCES[index]
        except ValueError:
            response = "The argument for the GET command must be a number from 0 to 4"
        except IndexError:
            response = "The argument for the GET command must be a number from 0 to 4"






    # -- The message has to be encoded into bytes. LA RESPUESTA SEIMPRE SE ENVIA DE ESTA MANERA
    cs.send(response.encode())    #cuando enviemos datos desde el servidor al cliente, siempre hay que codificarlo, y cualquier print en el servidor aparecerá en la termiinal(del servidor) , pero no quiere decir que el cliente sepa lo que ha pasado en el servidor . Si el servidor manda mensajes de vuelta, entonces si. con el .send el servidor puede mandar mensajes de vuelta

    # -- Close the data socket
    cs.close()