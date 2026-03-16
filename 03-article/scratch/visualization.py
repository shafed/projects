import os

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def plot_isotropy_heatmap(
    lsa_embeddings: np.ndarray,
    bert_embeddings: np.ndarray,
    n_samples: int = 200,
    save_path: str = "results/isotropy_heatmap.pdf",
) -> None:
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    n = min(n_samples, len(lsa_embeddings), len(bert_embeddings))
    idx = np.random.choice(len(lsa_embeddings), n, replace=False)

    sim_lsa = cosine_similarity(lsa_embeddings[idx])
    sim_bert = cosine_similarity(bert_embeddings[idx])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    im1 = ax1.imshow(sim_lsa, vmin=-1, vmax=1, cmap="coolwarm")
    ax1.set_title("LSA")
    plt.colorbar(im1, ax=ax1)

    im2 = ax2.imshow(sim_bert, vmin=-1, vmax=1, cmap="coolwarm")
    ax2.set_title("BERT")
    plt.colorbar(im2, ax=ax2)

    fig.suptitle("Cosine Similarity Heatmaps", fontsize=14)
    fig.tight_layout()
    plt.savefig(save_path, bbox_inches="tight", dpi=300)
    plt.close()
