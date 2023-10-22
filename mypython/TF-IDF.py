from vectorization import word_vectors, vocabulary  # Import the word vectors and vocabulary from the vectorization module
import numpy as np
import math

def calculate_tf(word_vector):
    total_words = len(word_vector)
    return sum(word_vector) / total_words

# Calculate IDF for the entire corpus
def calculate_idf(word, word_vectors):
    num_documents_with_word = np.sum(word_vectors[:, vocabulary.index(word)] > 0)
    total_documents = len(word_vectors)
    return math.log10(total_documents / (1 + num_documents_with_word))

# Convert 'word_vectors' to a NumPy array
word_vectors = np.array(word_vectors)

def calculate_tf_idf(word_vectors, vocabulary):
    tf_idf_scores = []
    for i, word_vector in enumerate(word_vectors):
        tf = calculate_tf(word_vector)
        idf = calculate_idf(vocabulary[i], word_vectors)
        tf_idf_scores.append((vocabulary[i], tf * idf))
    return tf_idf_scores

# Calculate TF-IDF for the word vectors
tf_idf_scores = calculate_tf_idf(word_vectors, vocabulary)

# Print TF-IDF scores
for word, score in tf_idf_scores:
    print(f"Word: {word}")
    print(f"TF-IDF Score: {score}")
