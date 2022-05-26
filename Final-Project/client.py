import json
import http.client
import termcolor

SERVER = "localhost:8080"

conn = http.client.HTTPConnection(SERVER)

def ask_server(ENDPOINT, PARAMS=""):
    try:
        conn = http.client.HTTPConnection(SERVER)
        conn.request("GET", ENDPOINT + PARAMS)
        response = conn.getresponse()
        data1 = response.read().decode("utf-8")
        data1 = json.loads(data1)
        return data1
    except ConnectionRefusedError:
        print("Error, unable to connect to the server")

termcolor.cprint("BASIC Level Services:", "blue")

termcolor.cprint("1)List of species:", "green")
species_list = ask_server("/listSpecies?","limit=20&json=on")
print(species_list)

termcolor.cprint("2)Karyotype information:", "green")
species_list = ask_server("/karyotype?", "species=human&json=on")
print(species_list)

termcolor.cprint("3)Chromosome length:", "green")
species_list = ask_server("/chromosomeLength?","chosen_species=mouse&chromosome=18&json=on")
print(species_list)

termcolor.cprint("MEDIUM Level Services:", "blue")

termcolor.cprint("4)Gene sequence:", "green")
species_list = ask_server("/geneSeq?", "seq=FRAT1&json=on")
print(species_list)

termcolor.cprint("5)Gene information:", "green")
species_list = ask_server("/geneInfo?", "info=FXN&json=on")
print(species_list)

termcolor.cprint("6)Gene calculations:", "green")
species_list = ask_server("/geneCalc?","calc=ADA&json=on")
print(species_list)

termcolor.cprint("7)Gene list:", "green")
species_list = ask_server("/geneList?", "chromo=9&start=22125500&end=22136000&json=on")
print(species_list)
