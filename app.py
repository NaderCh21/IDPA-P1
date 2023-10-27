import time
import xml.etree.ElementTree as ET
from flask import Flask, render_template, request, Response
from functions.vectorization import *
from functions.VSM_Similarity import *
from functions.preprocessing import *
from functions.indexing import *


app = Flask(__name__)

XMLpaths1 = [

    "XMLdocuments1/city1.xml",
    "XMLdocuments1/city2.xml",
    "XMLdocuments1/city3.xml",
    "XMLdocuments1/city4.xml",
    "XMLdocuments1/city5.xml",
    "XMLdocuments1/food1.xml",
    "XMLdocuments1/food2.xml",
    "XMLdocuments1/food3.xml",
    "XMLdocuments1/food4.xml",
    "XMLdocuments1/food5.xml",
    "XMLdocuments1/food6.xml",
    "XMLdocuments1/food7.xml",
    "XMLdocuments1/food8.xml",
    "XMLdocuments1/food9.xml",
    "XMLdocuments1/food10.xml",
    "XMLdocuments1/food11.xml",
    "XMLdocuments1/food12.xml",
    "XMLdocuments1/food13.xml",
    "XMLdocuments1/food14.xml",
    "XMLdocuments1/food15.xml",
    "XMLdocuments1/food16.xml",
    "XMLdocuments1/food17.xml",
    "XMLdocuments1/food18.xml",
    "XMLdocuments1/food19.xml",
    "XMLdocuments1/food20.xml",
    "XMLdocuments1/food21.xml",
    "XMLdocuments1/food22.xml",
    "XMLdocuments1/food23.xml",
    "XMLdocuments1/food24.xml",
    "XMLdocuments1/food25.xml",
    "XMLdocuments1/food26.xml",
    "XMLdocuments1/food27.xml",
    "XMLdocuments1/food28.xml",
    "XMLdocuments1/food29.xml",
    "XMLdocuments1/food30.xml",
    "XMLdocuments1/food31.xml",
    "XMLdocuments1/food32.xml",
    "XMLdocuments1/food33.xml",
    "XMLdocuments1/food34.xml",
    "XMLdocuments1/food35.xml",
    "XMLdocuments1/food36.xml",
]



vectors = getAllVectors(XMLpaths1)
indexTable = getIndexingTable(vectors)

pprint(indexTable)
roots = []
for path in XMLpaths1:
    tree = ET.parse(path)
    root = tree.getroot()
    roots.append(root)


@app.route("/", methods=("GET", "POST"))
def main():
    if request.method == "POST":
        timeBefore = time.time()
        queryVector = {}
        queryResult = []

        if request.form["queryType"] == "text":
            queryVector = getTextQueryVector(request.form["query"])
        else:
            tree = ET.ElementTree(ET.fromstring(request.form["query"]))
            root = tree.getroot()
            getVectorWithTF(root, "", queryVector)

        if request.form["simType"] == "VSM":
            newVectorList = getDocumentFromIndex(indexTable, queryVector, vectors)
            queryResult = getAllSimVSM(queryVector, newVectorList)
        

        timeAfter = time.time()

        print("Query Vector")
        pprint(queryVector)
        print("Query result")
        pprint(queryResult)

        timeTaken = round(timeAfter - timeBefore, 4)

        return render_template("result.html", queryResult=queryResult, time=timeTaken)

    return render_template("search.html")


@app.route("/<folder>/<doc>")
def getDoc1(folder, doc):
    tree = ET.parse(folder + "/" + doc)
    root = tree.getroot()
    xmlstr = ET.tostring(root, encoding="utf8", method="xml")
    return Response(xmlstr, mimetype="text/xml")
