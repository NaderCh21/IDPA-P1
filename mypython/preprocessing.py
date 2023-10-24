import nltk
# Download the necessary NLTK resources
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def preprocess_documents(documents):
    # Tokenization, removal of punctuation, and lowercase conversion
    tokens = [word_tokenize(doc) for doc in documents]
    tokens = [[word.lower() for word in doc if word.isalnum()] for doc in tokens]

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [[word for word in doc if word not in stop_words] for doc in tokens]

    # Stemming
    stemmer = PorterStemmer()
    tokens = [[stemmer.stem(word) for word in doc] for doc in tokens]

    return tokens

def create_term_context_matrix(tokens, context_window=2):
    # Build the term-context matrix
    term_context_matrix = {}

    # Loop over every token/word
    for doc_tokens in tokens:
        for i, target_word in enumerate(doc_tokens):
            term_context_matrix.setdefault(target_word, {})
            for j in range(max(0, i - context_window), min(i + context_window + 1, len(doc_tokens))):
                if i != j:
                    context_word = doc_tokens[j]
                    term_context_matrix[target_word][context_word] = term_context_matrix[target_word].get(context_word, 0) + 1

    return term_context_matrix

# Example usage
input_text = [
    'LAU is an American university in Lebanon. It is of the leading American universities in Lebanon.',
    'USJ is a French university in Lebanon. It is a leading university in Lebanon.',
    'LMA: the Lebanese military academy is the only military university in Lebanon.'
]

# Preprocess the input documents
preprocessed_input = preprocess_documents(input_text)

print("\ntokens:\n" , preprocessed_input)

# Create the term-context matrix
term_context_matrix = create_term_context_matrix(preprocessed_input)

# You can use this matrix for further processing, such as vectorization.
print("\nTerm-Context Matrix:\n", term_context_matrix)
