import string
import nltk

nltk.download("punkt")
nltk.download("stopwords")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def normalize_text(text):

    tokens = word_tokenize(text)
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
    # stem the words
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(word) for word in words]

    return stemmed

# Example usage
input_text = 'I like eating apples'
 
# Preprocess the input documents
normalized_input = normalize_text(input_text)

print("\ntokens:\n", normalized_input)
