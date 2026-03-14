import os

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

os.makedirs("results", exist_ok=True)


def plot_isotropy_heatmap(
    lsa_embeddings: np.ndarray,
    bert_embeddings: np.ndarray,
    n_samples: int = 200,
    save_path: str = "results/isotropy_heatmap.pdf",
) -> None:
    idx = np.random.choice(len(lsa_embeddings), n_samples, replace=False)
    lsa = [lsa_embeddings[i] for i in idx]
    bert = [bert_embeddings[i] for i in idx]
    sim_lsa = cosine_similarity(lsa, lsa)
    sim_bert = cosine_similarity(bert, bert)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(sim_lsa, vmin=-1, vmax=1, cmap="coolwarm", interpolation="bilinear")
    ax1.set_title("LSA")
    ax2.imshow(sim_bert, vmin=-1, vmax=1, cmap="coolwarm", interpolation="bilinear")
    ax2.set_title("BERT")
    plt.savefig(save_path, bbox_inches="tight")
