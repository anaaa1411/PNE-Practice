import http.client
import json


SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/ENSG00000207552'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS)
    # -- Read the response message from the server
    response = conn.getresponse()
    # -- Print the status line
    print(f"Response received!: {response.status} {response.reason}\n")
    # -- Read the response's body
    data1 = response.read().decode("utf-8")
    data1 = json.loads(data1)
    # -- Print the received data
    print(f"Gene: MIR633")
    print(f"Description: {data1['desc']}")
    print(f"Bases: {data1['seq']}")

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
