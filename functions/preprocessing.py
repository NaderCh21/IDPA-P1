import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
#nltk.download('averaged_perceptron_tagger')
#nltk.download("punkt")
#nltk.download("wordnet")
#nltk.download("stopwords")

def normalize_text(text):
    tokens = word_tokenize(text)
    tokens = [w.lower() for w in tokens]
    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()]
    stop_words = set(stopwords.words("english"))
    words = [w for w in words if not w in stop_words]
    
    lemmatize = []
    lemmatizer = WordNetLemmatizer()
    
    for word, tag in pos_tag(words):
        if tag.startswith("V"):  # Check if the word is a verb
            word = lemmatizer.lemmatize(word, 'v')
        elif tag.startswith("J"):  # Check if the word is an adjective
            word = lemmatizer.lemmatize(word, 'a')
        elif tag.startswith("N"):  # Check if the word is a noun
            word = lemmatizer.lemmatize(word, 'n')
        elif tag.startswith("R"):  # Check if the word is an adverb
            word = lemmatizer.lemmatize(word, 'r')
        
        lemmatize.append(word)
    
    return lemmatize

# Example usage
input_text = 'I like eating apples and drinking in lebaense universities'

# Preprocess the input documents
normalized_input = normalize_text(input_text)

print("\ntokens:\n", normalized_input)
