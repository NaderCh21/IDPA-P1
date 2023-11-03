# Import necessary libraries
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

# Download necessary datasets from nltk
nltk.download("averaged_perceptron_tagger")
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")


def normalize_text(text):
    # Tokenize the input text into individual words
    tokens = word_tokenize(text)

    # Convert all tokens to lowercase
    tokens = [w.lower() for w in tokens]

    # Create a translation table to remove punctuation
    table = str.maketrans("", "", string.punctuation)

    # Remove punctuation from each token using the translation table
    stripped = [w.translate(table) for w in tokens]

    # Filter out tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]

    # Define a set of English stopwords
    stop_words = set(stopwords.words("english"))

    # Remove stopwords from the list of tokens
    words = [w for w in words if not w in stop_words]

    # Initialize an empty list to store lemmatized words
    lemmatize = []

    # Initialize the WordNet lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Iterate over each word and its part-of-speech tag
    for word, tag in pos_tag(words):
        # Check the part-of-speech tag and lemmatize accordingly
        if tag.startswith("V"):  # Verb
            word = lemmatizer.lemmatize(word, "v")
        elif tag.startswith("J"):  # Adjective
            word = lemmatizer.lemmatize(word, "a")
        elif tag.startswith("N"):  # Noun
            word = lemmatizer.lemmatize(word, "n")
        elif tag.startswith("R"):  # Adverb
            word = lemmatizer.lemmatize(word, "r")

        # Append the lemmatized word to the list
        lemmatize.append(word)

    # Return the list of lemmatized words
    return lemmatize


# Example usage
input_text = "I like eating apples and drinking in lebanense universities"

# Preprocess the input text using the normalize_text function
normalized_input = normalize_text(input_text)

# Print the preprocessed text
print("\ntokens:\n", normalized_input)
