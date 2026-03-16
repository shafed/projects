import numpy as np
from scipy.stats import skew
from sklearn.neighbors import NearestNeighbors


def compute_participation_ratio(embeddings: np.ndarray) -> dict:
    cov = np.cov(embeddings, rowvar=False)
    lmbd = np.linalg.eigvalsh(cov)
    lmbd = np.maximum(lmbd, 0.0)
    s = lmbd.sum()
    s2 = (lmbd**2).sum()
    pr = (s**2) / s2 if s2 > 0 else 0.0
    return {"pr": float(pr)}


def compute_effective_rank(embeddings: np.ndarray) -> dict:
    sv = np.linalg.svd(embeddings, compute_uv=False)
    sv = sv[sv > 0]
    p = sv / sv.sum()
    H = -np.sum(p * np.log(p))
    return {"effective_rank": float(np.exp(H))}


def compute_isotropy(embeddings: np.ndarray) -> dict:
    cov = np.cov(embeddings, rowvar=False)
    lmbd = np.linalg.eigvalsh(cov)
    lmbd = lmbd[lmbd > 1e-12]
    if len(lmbd) == 0:
        return {"isotropy": 0.0}
    return {"isotropy": float(lmbd.min() / lmbd.max())}


def compute_hubness(embeddings: np.ndarray, k: int = 5) -> dict:
    nn = NearestNeighbors(n_neighbors=k + 1, metric="cosine", algorithm="brute")
    nn.fit(embeddings)
    _, indices = nn.kneighbors(embeddings)
    indices = indices[:, 1:]
    N_k = np.bincount(indices.ravel(), minlength=len(embeddings))
    return {"hubness": float(skew(N_k))}
