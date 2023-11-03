import math
from pprint import pprint
from .path_Sim import getSimPath


def calculate_similarity_vsm(query_vector, document_vector):
    num = 0

    for dimension1 in query_vector:
        term1 = dimension1[0]

        for dimension2 in document_vector:
            term2 = dimension2[0]
            if term1 == term2:
                sim_path = getSimPath(dimension1[1], dimension2[1])
                num = num + (
                    query_vector[dimension1] * document_vector[dimension2] * sim_path
                )

    sum_vector1 = 0
    sum_vector2 = 0
    for dimension in query_vector:
        sum_vector1 = sum_vector1 + query_vector[dimension] * 2

    for dimension in document_vector:
        sum_vector2 = sum_vector2 + document_vector[dimension] ** 2

    return num / math.sqrt(sum_vector1 * sum_vector2)


# The following method calculates the similarity of the query vector with each document in the
# list of document vectors provided and sorts them in decreasing order.
def calculate_all_similarities_vsm(query_vector, list_of_document_vectors):
    sim_list = []
    i = 0
    for path in list_of_document_vectors:
        sim = calculate_similarity_vsm(query_vector, list_of_document_vectors[path])
        sim_list.append((path, round(sim, 4)))
        i = i + 1

    return sorted(sim_list, key=lambda tuple: tuple[1], reverse=True)
