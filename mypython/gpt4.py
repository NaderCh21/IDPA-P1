from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download stopwords
# nltk.download('punkt')
# nltk.download('stopwords')

# Pre-processing function
def preprocess(doc):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    words = word_tokenize(doc)
    filtered = [ps.stem(w.lower()) for w in words if w.isalnum() and w.lower() not in stop_words]
    return filtered

# Sample documents
doc1 = "LAU is an American university in Lebanon. It is of the leading American universities in Lebanon."
doc2 = "USJ is a French university in Lebanon. It is a leading university in Lebanon."
doc3 = "LMA: the Lebanese military academy is the only military university in Lebanon."

# Pre-process the documents and print tokens
tokens1, tokens2, tokens3 = preprocess(doc1), preprocess(doc2), preprocess(doc3)
print(f"Tokens for doc1: {tokens1}")
print(f"Tokens for doc2: {tokens2}")
print(f"Tokens for doc3: {tokens3}")

# Combine tokens back into preprocessed string for TF-IDF vectorization
doc1, doc2, doc3 = ' '.join(tokens1), ' '.join(tokens2), ' '.join(tokens3)

# Ask user for TF-IDF setting
setting = input("Would you like to use 'tf', 'idf', or 'both'? ").strip().lower()

# Configure TF-IDF settings based on user input
use_idf = True
norm = 'l2'
if setting == 'tf':
    use_idf = False
    norm = None
elif setting == 'idf':
    use_idf = True
    norm = None
elif setting == 'both':
    use_idf = True
    norm = 'l2'
else:
    print("Invalid option. Using both TF and IDF.")

# Document Vectorization with TF-IDF
vectorizer = TfidfVectorizer(use_idf=use_idf, norm=norm)
tfidf_matrix = vectorizer.fit_transform([doc1, doc2, doc3])

# Get feature names
feature_names = vectorizer.get_feature_names_out()

# Display TF-IDF values with corresponding words
for i, doc_vector in enumerate(tfidf_matrix.toarray()):
    print(f"\nTF-IDF values for doc{i+1}:")
    for j, feature in enumerate(feature_names):
        print(f"{feature}: {doc_vector[j]}")

# Function to compute similarity based on user choice
def compute_similarity(matrix, method='cosine'):
    if method == 'cosine':
        return cosine_similarity(matrix, matrix)
    elif method == 'euclidean':
        return euclidean_distances(matrix, matrix)
    else:
        raise ValueError("Unknown method")

# Compute Similarity (Here you can choose the method: 'cosine' or 'euclidean')
similarity_method = input("\nChoose similarity method ('cosine' or 'euclidean'): ").strip().lower()
similarity_matrix = compute_similarity(tfidf_matrix, method=similarity_method)

print("\nSimilarity Matrix:", similarity_matrix)