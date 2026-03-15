import numpy as np
from data_loader import load_newsgroups
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize


class LSAEmbedder:
    def __init__(self, n_components: int = 100, random_state: int = 42):
        self.tfidf = TfidfVectorizer(sublinear_tf=True)
        self.svd = TruncatedSVD(n_components=n_components, random_state=random_state)

    def fit_transform(self, texts: list[str]) -> np.ndarray:
        tfidf_matrix = self.tfidf.fit_transform(texts)
        svd_matrix = self.svd.fit_transform(tfidf_matrix)
        return normalize(svd_matrix)

    def transform(self, texts: list[str]) -> np.ndarray:
        tfidf_matrix = self.tfidf.transform(texts)
        svd_matrix = self.svd.transform(tfidf_matrix)
        return normalize(svd_matrix)


class BERTEmbedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def fit_transform(self, texts: list[str]) -> np.ndarray:
        return self.model.encode(texts, normalize_embeddings=True)
