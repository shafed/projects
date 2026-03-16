import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize


class LSAEmbedder:
    def __init__(self, n_components: int = 300, random_state: int = 42):
        self.tfidf = TfidfVectorizer(sublinear_tf=True)
        self.svd = TruncatedSVD(n_components=n_components, random_state=random_state)

    def fit(self, texts: list[str]) -> "LSAEmbedder":
        tfidf_matrix = self.tfidf.fit_transform(texts)
        self.svd.fit(tfidf_matrix)
        return self

    def transform(self, texts: list[str]) -> np.ndarray:
        tfidf_matrix = self.tfidf.transform(texts)
        svd_matrix = self.svd.transform(tfidf_matrix)
        return normalize(svd_matrix)

    def fit_transform(self, texts: list[str]) -> np.ndarray:
        tfidf_matrix = self.tfidf.fit_transform(texts)
        svd_matrix = self.svd.fit_transform(tfidf_matrix)
        return normalize(svd_matrix)


class BERTEmbedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: list[str], batch_size: int = 128) -> np.ndarray:
        return self.model.encode(
            texts, batch_size=batch_size, normalize_embeddings=True
        )
