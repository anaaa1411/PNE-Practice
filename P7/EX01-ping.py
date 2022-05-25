import http.client
import json


SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
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
    print(f"CONTENT: {data1['ping']}")
    if data1['ping'] == 1:
        print("PING OK! The database is running!")
    else:
        print("ERROR! The database is not running!")

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
