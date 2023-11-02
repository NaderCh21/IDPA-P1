
from pprint import pprint


# Helper function to update the indexing table
def updateIndexingTable(out, term, path):
    if term in out:
        if path not in out[term]:
            out[term].append(path)
    else:
        out[term] = [path]


# Helper function to update the new vector list
def updateNewVectorList(newVectorList, term, indexTable, oldVectorList):
    if term in indexTable:
        for path in indexTable[term]:
            if path not in newVectorList:
                newVectorList[path] = oldVectorList[path]


# Main function to generate the indexing table
def getIndexingTable(listOfVectors):
    out = {}
    for path, vector in listOfVectors.items():
        for dimension in vector:
            term = dimension[0]
            updateIndexingTable(out, term, path)

    print("Indexing Table")
    pprint(out)
    return out


# Main function to get the document from the index
def getDocumentFromIndex(indexTable, queryVector, oldVectorList):
    newVectorList = {}
    for dimension in queryVector:  # Note: Typo in original code, should be "dimension"
        term = dimension[0]  # Note: Typo in original code, should be "dimension"
        updateNewVectorList(newVectorList, term, indexTable, oldVectorList)

    print("Document to query from indexing table")
    pprint(newVectorList)
    return newVectorList
