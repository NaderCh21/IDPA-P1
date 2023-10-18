import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

def preprocess(text):
    # Tokenization
    tokens = word_tokenize(text)

    # Remove punctuation and convert to lowercase
    tokens = [word.lower() for word in tokens if word.isalnum()]

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]

    # Convert to document vector using bag-of-words representation
    vectorizer = CountVectorizer()
    document_vector = vectorizer.fit_transform([' '.join(tokens)])

    return document_vector

# Example usage
input_text = "Let's test this sentence: DUCK DUCK DUCK ALLY ALLY SUPER SUPER SUPER SUPER. We should get out of it the following output: 2 3 1 1 1 1 1 4 1"
document_vector = preprocess(input_text)
print("Document Vector:\n", document_vector.toarray())

# preprocess is a function that takes a text as input and performs various preprocessing steps on it.
# Tokenization: word_tokenize breaks the text into words or tokens.
# Punctuation and Lowercasing: Punctuation is removed, and all words are converted to lowercase to ensure consistency.
# Stopword Removal: Common words like 'and', 'the', 'is' (stop words) are removed using a predefined stop words list.
# Stemming: Words are reduced to their root or base form using Porter stemming.
# Document Vectorization: The preprocessed tokens are converted into a document vector using the bag-of-words approach via CountVectorizer. 
# Each element in the vector represents the frequency of a word in the text.