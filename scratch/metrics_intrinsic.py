import numpy as np
from scipy.stats import skew
from sklearn.metrics.pairwise import cosine_similarity


def compute_participation_ratio(embeddings: np.ndarray) -> dict:
    matrix = np.cov(embeddings.T)
    lmbd = np.linalg.eigvalsh(matrix)
    pr = sum(lmbd) ** 2 / sum(lmbd**2)
    return {"pr": pr}


def compute_effective_rank(embeddings: np.ndarray) -> dict:
    linalg = np.linalg.svd(embeddings, compute_uv=False)
    p = linalg / sum(linalg)
    H = -(p * np.log(p)).sum()
    rank = np.exp(H)
    return {"effective_rank": rank}


def compute_isotropy(embeddings: np.ndarray) -> dict:
    variances = np.var(embeddings, axis=0)
    variances = variances[variances > 0]
    isotropy = min(variances) / max(variances)
    return {"isotropy": isotropy}


def compute_hubness(embeddings: np.ndarray, k: int = 10) -> dict:
    sim = cosine_similarity(embeddings, embeddings)
    neighbors = np.argsort(sim, axis=1)[:, -(k + 1) : -1]
    N_k = np.bincount(neighbors.flatten())
    hubness = skew(N_k)
    return {"hubness": hubness}
