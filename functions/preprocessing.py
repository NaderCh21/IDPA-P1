import string

import nltk

#nltk.download("punkt")
#nltk.download("wordnet")
#nltk.download("stopwords")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer 


def normalize_text(text):

    tokens = word_tokenize( text)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words("english"))
    words = [w for w in words if not w in stop_words]
    # lemantize
    lemantize = []
    #"v" for verbs
    #"a" for adjectives
    #"n" for nouns
    #"r" for adverbs
    for word in words:
        try:
            temp = wordnet.synsets(word)[0].pos()
            if temp == "v":
                word = WordNetLemmatizer().lemmatize(word, "v")
            if temp == "a":
                word = WordNetLemmatizer().lemmatize(word, "a")
            if temp == "n":
                word = WordNetLemmatizer().lemmatize(word, "n")
            if temp == "r":
                word = WordNetLemmatizer().lemmatize(word, "r")

            lemantize.append(word)
        except:
            lemantize.append(word)
            # If an exception occurs during the lemmatization attempt, it defaults to just keeping the original word.

    return lemantize


# Example usage
input_text = 'I like eating apple'
 
# Preprocess the input documents
normalized_input = normalize_text(input_text)

print("\ntokens:\n" , normalized_input)

