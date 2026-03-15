import numpy as np
from scipy.stats import spearmanr
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import adjusted_rand_score, f1_score, silhouette_score
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import cross_val_score


def compute_sts(embeddings1: np.ndarray, embeddings2: np.ndarray, scores: list) -> dict:
    sim = cosine_similarity(embeddings1, embeddings2)
    spearman = spearmanr(np.diag(sim), scores)

    return {"spearman": spearman.statistic}


def compute_classification(embeddings: np.ndarray, labels: np.ndarray) -> dict:
    clf = LogisticRegression(max_iter=1000, random_state=42)
    accuracy = cross_val_score(clf, embeddings, labels, cv=5, scoring="accuracy")
    f1_macro = cross_val_score(clf, embeddings, labels, cv=5, scoring="f1_macro")
    return {"accuracy": accuracy.mean(), "f1_macro": f1_macro.mean()}


def compute_clustering(embeddings: np.ndarray, labels: np.ndarray) -> dict:
    cluster = KMeans(len(np.unique(labels)), random_state=42)
    pred_labels = cluster.fit_predict(embeddings)
    ari = adjusted_rand_score(labels, pred_labels)
    silhouette = silhouette_score(embeddings, pred_labels)
    return {"ari": ari, "silhouette": silhouette}


def compute_paraphrase(
    embeddings1: np.ndarray, embeddings2: np.ndarray, labels: list
) -> dict:
    sim = cosine_similarity(embeddings1, embeddings2)
    pred = (sim >= 0.5).astype(int)
    f1 = f1_score(labels, np.diag(pred))
    return {"f1": f1}
