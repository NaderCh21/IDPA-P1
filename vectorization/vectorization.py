import numpy as np

# Function to create vector representations from the term-context matrix
def create_word_vectors(term_context_matrix):
    # Create a list of unique words (vocabulary)
    vocabulary = sorted(term_context_matrix.keys())

    # Create an empty matrix for word vectors
    word_vectors = []

    for word in vocabulary:
        # Create a vector for each word
        vector = [term_context_matrix[word].get(context_word, 0) for context_word in vocabulary]
        word_vectors.append(vector)

    return np.array(word_vectors)

# Example usage
term_context_matrix = {
    'cat': {'dog': 1},
    'dog': {'cat': 1, 'brown': 1},
    'brown': {'dog': 1},
    'black': {'cat': 1}
}

word_vectors = create_word_vectors(term_context_matrix)

# Now you have numerical vector representations for words
print("Word Vectors:\n", word_vectors)
