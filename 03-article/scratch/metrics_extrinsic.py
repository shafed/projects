import numpy as np
from scipy.stats import spearmanr
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    adjusted_rand_score,
    f1_score,
    silhouette_score,
)


def compute_sts(e1: np.ndarray, e2: np.ndarray, scores: list) -> dict:
    cos = np.sum(e1 * e2, axis=1)
    rho, p = spearmanr(cos, scores)
    return {"spearman": rho, "p_value": p}


def compute_classification(
    X_train: np.ndarray,
    X_test: np.ndarray,
    y_train: np.ndarray,
    y_test: np.ndarray,
) -> dict:
    clf = LogisticRegression(max_iter=1000, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "f1_macro": f1_score(y_test, y_pred, average="macro"),
    }


def compute_clustering(embeddings: np.ndarray, labels: np.ndarray) -> dict:
    n_clusters = len(np.unique(labels))
    km = KMeans(n_clusters=n_clusters, n_init=10, random_state=42)
    pred = km.fit_predict(embeddings)
    ari = adjusted_rand_score(labels, pred)
    sil = silhouette_score(embeddings, pred, metric="cosine")
    return {"ari": ari, "silhouette": sil}


def compute_paraphrase(e1: np.ndarray, e2: np.ndarray, labels: list) -> dict:
    cos = np.sum(e1 * e2, axis=1)
    labels = np.array(labels)
    best_f1, best_th = 0.0, 0.5
    for th in np.arange(0.0, 1.01, 0.01):
        pred = (cos >= th).astype(int)
        f = f1_score(labels, pred, zero_division=0)
        if f > best_f1:
            best_f1, best_th = f, th
    return {"f1": best_f1, "optimal_threshold": best_th}
