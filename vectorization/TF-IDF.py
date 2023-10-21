from vectorization import word_vectors  # Import the word vectors from the vectorization module
import numpy as np

# Import the word vectors using the import_word_vectors function
word_vectors = import_word_vectors()

def calculate_tf(word_vector):
    total_words = len(word_vector)
    return sum(word_vector) / total_words

def calculate_idf(word, word_vectors):
    num_documents_with_word = sum(1 for vector in word_vectors.values() if word in vector)
    total_documents = len(word_vectors)
    return math.log10(total_documents / (1 + num_documents_with_word))

def calculate_tf_idf(word_vectors):
    tf_idf_scores = {}
    for word in word_vectors:
        tf = calculate_tf(word_vectors[word])
        idf = calculate_idf(word, word_vectors)
        tf_idf_scores[word] = tf * idf
    return tf_idf_scores

# Calculate TF-IDF for the word vectors
tf_idf_scores = calculate_tf_idf(word_vectors)

# Print TF-IDF scores
for word, score in tf_idf_scores.items():
    print(f"{word}: {score}")
