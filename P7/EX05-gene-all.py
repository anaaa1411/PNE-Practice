import http.client
import json
from Seq1 import Seq

def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1
    total = sum(d.values())
    for k, v in d.items():
        d[k] = [v, (v * 100) / total]
    return d

def convert_message(base_count):
    message = ""
    for k,v in base_count.items():
        message += k + ": " + str(v[0]) + " (" + str(round(v[1],1)) + "%)" + "\n"
    return message

def info_operation(arg):
    base_count = count_bases(arg)
    response = convert_message(base_count)
    return response




GENES = {"FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"}

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS


# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)


for gene in GENES:
    try:
        conn.request("GET", ENDPOINT + GENES[gene] + PARAMS)
        # -- Read the response message from the server
        response = conn.getresponse()
        # -- Print the status line
        print(f"Server: {SERVER}")
        print(f"URL: {URL}")
        print(f"Response received!: {response.status} {response.reason}\n")
        # -- Read the response's body
        data1 = response.read().decode("utf-8")
        data1 = json.loads(data1)
        # -- Print the received data
        print(f"Gene: {gene}")
        print(f"Description: {data1['desc']}")
        sequence = Seq(data1['seq'])
        print(f"Total length: {sequence.len()}")
        print(f"{info_operation(str(sequence))}", end="")
        print(f"Most frequent Base:{sequence.seq_frequent_base()}\n")

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
