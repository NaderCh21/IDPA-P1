import nltk
# Download the necessary NLTK resource
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def create_term_context_matrix(documents, context_window=2):
    # Tokenization
    tokens = [word_tokenize(doc) for doc in documents]

    # Remove punctuation and convert to lowercase
    tokens = [[word.lower() for word in doc if word.isalnum()] for doc in tokens]

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [[word for word in doc if word not in stop_words] for doc in tokens]

    # Stemming
    stemmer = PorterStemmer()
    tokens = [[stemmer.stem(word) for word in doc] for doc in tokens]

    # Build the term-context matrix
    term_context_matrix = {}
    for doc_tokens in tokens:
        for i, target_word in enumerate(doc_tokens):
            term_context_matrix.setdefault(target_word, {})
            for j in range(max(0, i - context_window), min(i + context_window + 1, len(doc_tokens))):
                if i != j:
                    context_word = doc_tokens[j]
                    term_context_matrix[target_word][context_word] = term_context_matrix[target_word].get(context_word, 0) + 1

    return term_context_matrix

# Example usage
input_texts = [
    "LAU is an American university located in Lebanon. It is one of the leading American universities in Lebanon.",
    "USJ is a French university founded in Lebanon. It is a leading university in Lebanon.",
    "LMA: the Lebanese military academy is the only military university in Lebanon.",
]

term_context_matrix = create_term_context_matrix(input_texts)
# You can use this matrix for further processing, such as vectorization.
print("Term-Context Matrix:\n", term_context_matrix)
