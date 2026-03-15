import numpy as np
from data_loader import load_all
from metrics_extrinsic import *
from metrics_intrinsic import *
from models import BERTEmbedder, LSAEmbedder
from visualization import plot_isotropy_heatmap


def generate_embeddings(data: dict) -> dict:
    bert = BERTEmbedder()
    lsa = LSAEmbedder()
    texts, labels = data["newsgroups"]
    lsa_newsgroups = LSAEmbedder().fit_transform(texts)
    bert_newsgroups = BERTEmbedder().fit_transform(texts)

    s1, s2, scores = data["stsb"]
    lsa.fit_transform(s1 + s2)
    lsa_stsb_1 = lsa.transform(s1)
    lsa_stsb_2 = lsa.transform(s2)
    bert_stsb_1 = bert.fit_transform(s1)
    bert_stsb_2 = bert.fit_transform(s2)

    s1, s2, scores = data["mrpc"]
    lsa.fit_transform(s1 + s2)
    lsa_mrpc_1 = lsa.transform(s1)
    lsa_mrpc_2 = lsa.transform(s2)
    bert_mrpc_1 = bert.fit_transform(s1)
    bert_mrpc_2 = bert.fit_transform(s2)
    return {
        "lsa_newsgroups": lsa_newsgroups,
        "bert_newsgroups": bert_newsgroups,
        "lsa_stsb_1": lsa_stsb_1,
        "bert_stsb_1": bert_stsb_1,
        "lsa_stsb_2": lsa_stsb_2,
        "bert_stsb_2": bert_stsb_2,
        "lsa_mrpc_1": lsa_mrpc_1,
        "bert_mrpc_1": bert_mrpc_1,
        "lsa_mrpc_2": lsa_mrpc_2,
        "bert_mrpc_2": bert_mrpc_2,
    }


def run_intrinsic(embeddings: dict) -> dict:
    lsa_newsgroups = embeddings["lsa_newsgroups"]
    bert_newsgroups = embeddings["bert_newsgroups"]

    pr_lsa = compute_participation_ratio(lsa_newsgroups)
    pr_bert = compute_participation_ratio(bert_newsgroups)
    effective_rank_lsa = compute_effective_rank(lsa_newsgroups)
    effective_rank_bert = compute_effective_rank(bert_newsgroups)
    isotropy_lsa = compute_isotropy(lsa_newsgroups)
    isotropy_bert = compute_isotropy(bert_newsgroups)
    hubness_lsa = compute_hubness(lsa_newsgroups)
    hubness_bert = compute_hubness(bert_newsgroups)
    return {
        "lsa": {
            **pr_lsa,
            **effective_rank_lsa,
            **isotropy_lsa,
            **hubness_lsa,
        },
        "bert": {
            **pr_bert,
            **effective_rank_bert,
            **isotropy_bert,
            **hubness_bert,
        },
    }


def run_extrinsic(embeddings: dict, data: dict) -> dict:
    lsa_stsb_1 = embeddings["lsa_stsb_1"]
    bert_stsb_1 = embeddings["bert_stsb_1"]
    lsa_stsb_2 = embeddings["lsa_stsb_2"]
    bert_stsb_2 = embeddings["bert_stsb_2"]
    _, _, scores = data["stsb"]

    spearman_lsa = compute_sts(lsa_stsb_1, lsa_stsb_2, scores)
    spearman_bert = compute_sts(bert_stsb_1, bert_stsb_2, scores)

    lsa_newsgroups = embeddings["lsa_newsgroups"]
    bert_newsgroups = embeddings["bert_newsgroups"]
    _, labels = data["newsgroups"]

    accuracy_f1_macro_lsa = compute_classification(lsa_newsgroups, labels)
    accuracy_f1_macro_bert = compute_classification(bert_newsgroups, labels)
    ari_silhouette_lsa = compute_clustering(lsa_newsgroups, labels)
    ari_silhouette_bert = compute_clustering(bert_newsgroups, labels)

    lsa_mrpc_1 = embeddings["lsa_mrpc_1"]
    bert_mrpc_1 = embeddings["bert_mrpc_1"]
    lsa_mrpc_2 = embeddings["lsa_mrpc_2"]
    bert_mrpc_2 = embeddings["bert_mrpc_2"]
    _, _, labels = data["mrpc"]

    f1_lsa = compute_paraphrase(lsa_mrpc_1, lsa_mrpc_2, labels)
    f1_bert = compute_paraphrase(bert_mrpc_1, bert_mrpc_2, labels)
    return {
        "lsa": {
            **spearman_lsa,
            **accuracy_f1_macro_lsa,
            **ari_silhouette_lsa,
            **f1_lsa,
        },
        "bert": {
            **spearman_bert,
            **accuracy_f1_macro_bert,
            **ari_silhouette_bert,
            **f1_bert,
        },
    }


def lsa_sensitivity(data: dict) -> None:
    for k in [50, 100, 200, 300, 500]:
        lsa = LSAEmbedder(k)
        s1, s2, scores = data["stsb"]
        lsa.fit_transform(s1 + s2)
        e1 = lsa.transform(s1)
        e2 = lsa.transform(s2)
        res = compute_sts(e1, e2, scores)
        with open("results/sensitivity.dat", "a") as f:
            f.write(f"{k} {res['spearman']:.3f}\n")


def write_value_to_tex(data: dict) -> None:
    emb = generate_embeddings(data)

    intrinsic = run_intrinsic(emb)
    lsa = intrinsic["lsa"]
    bert = intrinsic["bert"]
    with open("results/numbers.tex", "a") as f:
        f.write(f"\\newcommand{{\\LSApr}}{{{lsa['pr']:.3f}}}\n")
        f.write(f"\\newcommand{{\\BERTpr}}{{{bert['pr']:.3f}}}\n")
        f.write(f"\\newcommand{{\\LSAeffectiverank}}{{{lsa['effective_rank']:.3f}}}\n")
        f.write(
            f"\\newcommand{{\\BERTeffectiverank}}{{{bert['effective_rank']:.3f}}}\n"
        )
        f.write(f"\\newcommand{{\\LSAisotropy}}{{{lsa['isotropy']:.3f}}}\n")
        f.write(f"\\newcommand{{\\BERTisotropy}}{{{bert['isotropy']:.3f}}}\n")
        f.write(f"\\newcommand{{\\LSAhubness}}{{{lsa['hubness']:.3f}}}\n")
        f.write(f"\\newcommand{{\\BERThubness}}{{{bert['hubness']:.3f}}}\n")

    extrinsic = run_extrinsic(emb, data)
    lsa = extrinsic["lsa"]
    bert = extrinsic["bert"]
    with open("results/numbers.tex", "a") as f:
        f.write(f"\\newcommand{{\\LSAspearman}}{{{lsa['spearman']:.3f}}}\n")
        f.write(f"\\newcommand{{\\BERTspearman}}{{{bert['spearman']:.3f}}}\n")
        f.write(f"\\newcommand{{\\LSAaccuracy}}{{{lsa['accuracy']:.3f}}}\n")
        f.write(f"\\newcommand{{\\BERTaccuracy}}{{{bert['accuracy']:.3f}}}\n")
        f.write(f"\\newcommand{{\\LSAf1_macro}}{{{lsa['f1_macro']:.3f}}}\n")
        f.write(f"\\newcommand{{\\BERTf1_macro}}{{{bert['f1_macro']:.3f}}}\n")
        f.write(f"\\newcommand{{\\LSAari}}{{{lsa['ari']:.3f}}}\n")
        f.write(f"\\newcommand{{\\BERTari}}{{{bert['ari']:.3f}}}\n")
        f.write(f"\\newcommand{{\\LSAsilhouette}}{{{lsa['silhouette']:.3f}}}\n")
        f.write(f"\\newcommand{{\\BERTsilhouette}}{{{bert['silhouette']:.3f}}}\n")
        f.write(f"\\newcommand{{\\LSAf1}}{{{lsa['f1']:.3f}}}\n")
        f.write(f"\\newcommand{{\\BERTf1}}{{{bert['f1']:.3f}}}\n")


def save_spectrum_data(embeddings: dict) -> None:
    lsa_newsgroups = embeddings["lsa_newsgroups"]
    bert_newsgroups = embeddings["bert_newsgroups"]
    lsa = np.linalg.svd(lsa_newsgroups, compute_uv=False)
    lsa = lsa / lsa[0]
    bert = np.linalg.svd(bert_newsgroups, compute_uv=False)
    bert = bert / bert[0]
    with open("results/spectrum.dat", "w") as f:
        f.write("i lsa bert\n")
        for i, (l, b) in enumerate(zip(lsa, bert), start=1):
            f.write(f"{i} {l} {b}\n")


data = load_all()
emb = generate_embeddings(data)
# write_value_to_tex(data)
# lsa_sensitivity(data)
save_spectrum_data(emb)
# plot_isotropy_heatmap(emb["lsa_newsgroups"], emb["bert_newsgroups"])
