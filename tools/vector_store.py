from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

vectorizer = None
matrix = None
stored_texts = None


def create_index(texts):
    global vectorizer, matrix, stored_texts

    stored_texts = texts

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(texts)

    return matrix, texts


def search_index(index, texts, query):

    query_vec = vectorizer.transform([query])

    scores = (matrix @ query_vec.T).toarray().ravel()

    top_idx = np.argsort(scores)[-3:]

    results = [texts[i] for i in top_idx]

    return "\n".join(results)