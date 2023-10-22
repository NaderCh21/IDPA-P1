import numpy as np
from preprocessing import term_context_matrix

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

    return word_vectors, vocabulary  # Return both word vectors and vocabulary

# Example usage
word_vectors, vocabulary = create_word_vectors(term_context_matrix)

# Now you have numerical vector representations for words and a list of corresponding words
for word, vector in zip(vocabulary, word_vectors):
    print(f"Word: {word}")
    print(f"Vector: {vector}")
