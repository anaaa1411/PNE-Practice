import http.server
import socketserver
import termcolor
import json
import http.client
import jinja2 as j
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from Seq1 import Seq

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
HTML_FOLDER = "./html/"
PORT = 8080

def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

def ensembl_request(endpoint, PARAMS=""):
    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)
    try:
        PARAMETERS = '?content-type=application/json'
        conn.request("GET", endpoint + PARAMETERS + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    response = conn.getresponse()
    print(f"Response received!: {response.status} {response.reason}\n")
    data1 = response.read().decode("utf-8")
    data1 = json.loads(data1)
    return data1

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
        message += k + ": " + str(v[0]) + " (" + str(round(v[1],1)) + "%)" + "<br>"
    return message
def info_operation(arg):
    base_count = count_bases(arg)
    response = convert_message(base_count)
    return response


socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print("The old path was", self.path)
        print("The new path is", url_path.path)
        print("arguments", arguments)

        if self.path == "/":
            contents = read_html_file("index.html")\
                .render()
    #BASIC LEVEL:

        elif path == "/listSpecies": #Ex1
            try:
                limit = int(arguments["limit"][0])
                dict_ans = ensembl_request("/info/species", "")
                species_list = dict_ans["species"]
                species_list_def = []
                for i in range(0,limit):
                    species_list_def.append(species_list[i]["display_name"])
                if "json" in arguments:
                    contents = {"limit": limit,"length": len(species_list),"species_list": species_list_def}
                else:
                    contents = read_html_file(path[1:] + ".html").\
                        render(context={"limit": limit,"length": str(len(species_list)),"species": species_list_def})
            except (IndexError,ValueError):
                if "json" in arguments:
                    contents = {"error": "Wrong value.Try entering a value inside the limits 0-311, or leaving the text box empty for getting a list of all the species."}
                else:
                    contents = read_html_file("error.html").render()
            except KeyError:
                dict_ans = ensembl_request("/info/species", "")
                species_list = dict_ans["species"]
                species_list_empty = []
                for i in range(0, int(len(species_list))):
                    species_list_empty.append(species_list[i]["display_name"])
                if "json" in arguments:
                    contents={"all_species": species_list_empty}
                else:
                    contents = read_html_file(path[1:] + ".html"). \
                        render(context={"empty": species_list_empty})

        elif path == "/karyotype": #Ex2
            try:
                species = str(arguments["species"][0])
                dict_ans = ensembl_request("/info/assembly/" + species, "")
                karyotype_list = dict_ans["karyotype"]
                if "json" in arguments:
                    contents = {"karyotype": karyotype_list}
                else:
                    contents = read_html_file(path[1:] + ".html").\
                        render(context={"karyotype": karyotype_list})
            except KeyError:
                if "json" in arguments:
                    contents = {"error": "Wrong values entered or no information of them on ensmbl."}
                else:
                    contents = read_html_file("error.html").render()

        elif path == "/chromosomeLength": #Ex3
            try:
                chosen_species = arguments["chosen_species"][0]
                our_chromosome = arguments["chromosome"][0]
                dict_ans = ensembl_request("/info/assembly/" + chosen_species, "")
                all_dict = dict_ans["top_level_region"]
                exit = False
                i = 0
                while not exit and i <len(all_dict):
                    chromosome = all_dict[i]
                    if chromosome["name"] == our_chromosome:
                        exit = True
                    i += 1
                if exit:
                    if "json" in arguments:
                        contents = {"chromosome_length": chromosome["length"]}
                    else:
                        contents = read_html_file(path[1:] + ".html"). \
                            render(context={"chromosome": chromosome["length"]})
                else:
                    if "json" in arguments:
                        contents = {"error": "Wrong values entered or no information of them on ensmbl."}
                    else:
                        contents = read_html_file("error.html").render()
            except (KeyError,IndexError):
                if "json" in arguments:
                    contents = {"error": "Wrong values entered or no information of them on ensmbl."}
                else:
                    contents = read_html_file("error.html").render()


    #MEDIUM LEVEL:

        elif path == "/geneSeq": #Ex4
            try:
                gen = str(arguments["seq"][0])
                key = GENES[gen]
                dict_ans = ensembl_request("/sequence/id/" + str(key), "")
                seq = dict_ans["seq"]
                if "json" in arguments:
                    contents = {"seq": seq}
                else:
                    contents = read_html_file(path[1:] + ".html").\
                        render(context={"seq": seq})
            except KeyError:
                if "json" in arguments:
                    contents = {"error": "Wrong values entered or no information of them on ensmbl."}
                else:
                    contents = read_html_file("error.html").render()

        elif path == "/geneInfo": #Ex5
            try:
                gen = str(arguments["info"][0])
                key = GENES[gen]
                dict_ans = ensembl_request("/sequence/id/" + str(key), "")
                desc = dict_ans["desc"].split(":")
                length = int(desc[4])-int(desc[3])
                if "json" in arguments:
                    contents = {"name": gen, "id": key, "length": length, "start": desc[3], "end": desc[4]}
                else:
                    contents = read_html_file(path[1:] + ".html").\
                        render(context={"start": desc[3], "end": desc[4], "name":gen, "id": key, "length": length})
            except KeyError:
                if "json" in arguments:
                    contents = {"error": "Wrong values entered or no information of them on ensmbl."}
                else:
                    contents = read_html_file("error.html").render()

        elif path == "/geneCalc": #Ex6
            try:
                gen = str(arguments["calc"][0])
                key = GENES[gen]
                dict_ans = ensembl_request("/sequence/id/" + str(key), "")
                sequence = dict_ans["seq"]
                s = Seq(sequence)
                if "json" in arguments:
                    contents = {"length": s.len(), "info": info_operation(sequence)}
                else:
                    contents = read_html_file(path[1:] + ".html").\
                        render(context={"length": s.len(), "info": info_operation(sequence)})
            except KeyError:
                if "json" in arguments:
                    contents = {"error": "Wrong values entered or no information of them on ensmbl."}
                else:
                    contents = read_html_file("error.html").render()

        elif path == "/geneList": #Ex7
            try:
                chromo = arguments["chromo"][0]
                start = arguments["start"][0]
                end = arguments["end"][0]
                point = chromo + ":" + start + "-" + end
                dict_ans = ensembl_request("/phenotype/region/homo_sapiens/" + point, ";feature_type=Variation")
                gene_list = []
                for d in dict_ans:
                    dict_gene = d
                    if "phenotype_associations" in dict_gene:
                        for d in dict_gene["phenotype_associations"]:
                            if "attributes" in d:
                                if "associated_gene" in d["attributes"]:
                                    gene_list.append(d["attributes"]["associated_gene"])
                if gene_list == []:
                    if "json" in arguments:
                        contents = {"error": "Wrong values entered or no information of them on ensmbl."}
                    else:
                        contents = read_html_file("error.html").render()
                else:
                    if "json" in arguments:
                        contents = {"genelist": gene_list}
                    else:
                        contents = read_html_file(path[1:] + ".html").\
                            render(context={"chromo": gene_list})
            except KeyError:
                if "json" in arguments:
                    contents = {"error": "Wrong values entered or no information of them on ensmbl."}
                else:
                    contents = read_html_file("error.html").render()

        else:
            if "json" in arguments:
                contents = {"error": "Wrong values entered or no information of them on ensmbl."}
            else:
                contents = read_html_file("error.html").render()


        self.send_response(200)  # -- Status line: OK!

        if "json" in arguments.keys():
            contents = json.dumps(contents)
            self.send_header('Content-Type', 'application/json')

        else:
            self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        self.end_headers()

        self.wfile.write(contents.encode())

        return

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
