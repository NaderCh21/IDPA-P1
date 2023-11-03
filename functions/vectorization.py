# Importing necessary libraries and modules
import xml.etree.ElementTree as ET  # For XML parsing
import math  # For mathematical operations
from preprocessing import *  # Importing all functions from preprocessing module
from pprint import pprint  # For pretty printing

# Wd(ti) = TF(ti, D) * IDF(ti, C)
# TF = frequency
# IDF(ti,D) = log (N/DF)      N: nb of indexing nodes in D
# DF(ti,D) is the number of indexing node elements in D containing ti
# t term and D document
# C document collection

# the following method will return a dictionary of an XML tree
# the dictionary will represent the vector of the XML document following the
# term context model
# the key is a tuple (term, path) and the value is the TF
# another method will be used if IDF is needed


# Function to get the vector with term frequency (TF) for XML data
def getVectorWithTF(root, path, vector):
    path = path + "/" + root.tag  # Constructing the path with the current XML tag
    attributeDict = root.attrib  # Getting attributes of the current XML tag

    # Handling the current tag, its text, and its attributes
    _handle_tags(root.tag, path, vector)
    _handle_text(root.text, path, vector)
    _handle_attributes(attributeDict, path, vector)

    # Recursively processing child tags
    for child in root:
        getVectorWithTF(child, path, vector)


# Function to handle XML tags and update the vector
def _handle_tags(tag, path, vector):
    tagPath = path  # Path for the current tag
    wordlist = normalize_text(tag)  # Normalizing the tag text
    _update_vector(
        wordlist, tagPath, vector
    )  # Updating the vector with normalized words


# Function to handle text inside XML tags and update the vector
def _handle_text(text, path, vector):
    if text:  # Check if text is not empty
        wordPath = path + "/#"  # Constructing path for the text
        wordlist = normalize_text(text)  # Normalizing the text
        _update_vector(
            wordlist, wordPath, vector
        )  # Updating the vector with normalized words
    else:
        print("not text")


# Function to handle attributes of XML tags and update the vector
def _handle_attributes(attributeDict, path, vector):
    for att in attributeDict:  # Iterating through each attribute
        attributePath = path + "/" + att + "/@"  # Constructing path for the attribute
        wordlist = normalize_text(attributeDict[att])  # Normalizing the attribute value
        _update_vector(
            wordlist, attributePath, vector
        )  # Updating the vector with normalized words


# Function to update the vector with normalized words
def _update_vector(wordlist, path, vector):
    for word in wordlist:  # Iterating through each word in the wordlist
        dimension = (word, path)  # Creating a tuple of word and its path
        # Incrementing the count of the word in the vector or initializing it to 1 if not present
        vector[dimension] = vector.get(dimension, 0) + 1


# Function to get the vector for a text query
def getTextQueryVector(text):
    vector = {}  # Initializing an empty vector
    wordlist = normalize_text(text)  # Normalizing the query text
    _update_vector(wordlist, "", vector)  # Updating the vector with normalized words
    return vector  # Returning the vector


# Function to calculate document frequency (DF) for a dimension
def DF(dimension, listOfVectors):
    # Counting the number of vectors containing the dimension
    return sum(1 for vector in listOfVectors.values() if dimension in vector)


# Function to calculate inverse document frequency (IDF) for all vectors
def IDF(listOfVectors):
    for vector in listOfVectors.values():  # Iterating through each vector
        for dimension in vector:  # Iterating through each dimension in the vector
            # Multiplying the term frequency with the IDF value
            vector[dimension] *= math.log(
                len(listOfVectors) / DF(dimension, listOfVectors)
            )


# Function to get vectors for all XML files provided in the list
def getAllVectors(XMLpaths):
    listOfVectors = {}  # Initializing an empty dictionary to store vectors
    for xmlfile in XMLpaths:  # Iterating through each XML file path
        print(xmlfile)  # Printing the current XML file path
        tree = ET.parse(xmlfile)  # Parsing the XML file
        root = tree.getroot()  # Getting the root tag of the XML
        vector = {}  # Initializing an empty vector
        getVectorWithTF(
            root, "", vector
        )  # Getting the vector with term frequency for the XML data
        listOfVectors[xmlfile] = vector  # Storing the vector in the dictionary

    # Printing vectors with only term frequency
    print("Vectors with only TF")
    pprint(listOfVectors)
    IDF(listOfVectors)  # Calculating IDF for all vectors
    # Printing vectors with both term frequency and inverse document frequency
    print("Vectors with TF and IDF")
    pprint(listOfVectors)
    return listOfVectors  # Returning the list of vectors


# Main execution block
if __name__ == "__main__":
    XMLpaths = [
        "XMLdocuments1/city1.xml",
        "XMLdocuments1/city2.xml",
    ]  # List of XML file paths
    getAllVectors(XMLpaths)  # Getting vectors for all XML files
    query = getTextQueryVector(
        "I like to eat apples"
    )  # Getting the vector for a text query
    pprint(query)  # Printing the query vector
