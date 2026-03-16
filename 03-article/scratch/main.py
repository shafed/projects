import os

import numpy as np

from data_loader import load_all
from metrics_extrinsic import (
    compute_classification,
    compute_clustering,
    compute_paraphrase,
    compute_sts,
)
from metrics_intrinsic import (
    compute_effective_rank,
    compute_hubness,
    compute_isotropy,
    compute_participation_ratio,
)
from models import BERTEmbedder, LSAEmbedder
from visualization import plot_isotropy_heatmap

os.makedirs("../results", exist_ok=True)


def generate_embeddings(data: dict) -> dict:
    bert = BERTEmbedder()
    ng = data["newsgroups"]

    # ── 20 Newsgroups: fit на train, transform train+test ──
    lsa_ng = LSAEmbedder()
    lsa_ng_train = lsa_ng.fit_transform(ng["train_texts"])
    lsa_ng_test = lsa_ng.transform(ng["test_texts"])
    bert_ng_train = bert.encode(ng["train_texts"])
    bert_ng_test = bert.encode(ng["test_texts"])

    # ── STS-B: fit на всех уникальных предложениях ──
    s1, s2, _ = data["stsb"]
    lsa_sts = LSAEmbedder()
    lsa_sts.fit(list(set(s1 + s2)))
    lsa_stsb_1 = lsa_sts.transform(s1)
    lsa_stsb_2 = lsa_sts.transform(s2)
    bert_stsb_1 = bert.encode(s1)
    bert_stsb_2 = bert.encode(s2)

    # ── MRPC: fit на всех уникальных предложениях ──
    s1, s2, _ = data["mrpc"]
    lsa_mr = LSAEmbedder()
    lsa_mr.fit(list(set(s1 + s2)))
    lsa_mrpc_1 = lsa_mr.transform(s1)
    lsa_mrpc_2 = lsa_mr.transform(s2)
    bert_mrpc_1 = bert.encode(s1)
    bert_mrpc_2 = bert.encode(s2)

    return {
        "lsa_ng_train": lsa_ng_train,
        "lsa_ng_test": lsa_ng_test,
        "bert_ng_train": bert_ng_train,
        "bert_ng_test": bert_ng_test,
        "lsa_stsb_1": lsa_stsb_1,
        "lsa_stsb_2": lsa_stsb_2,
        "bert_stsb_1": bert_stsb_1,
        "bert_stsb_2": bert_stsb_2,
        "lsa_mrpc_1": lsa_mrpc_1,
        "lsa_mrpc_2": lsa_mrpc_2,
        "bert_mrpc_1": bert_mrpc_1,
        "bert_mrpc_2": bert_mrpc_2,
    }


def run_intrinsic(emb: dict) -> dict:
    results = {}
    for name, key in [("lsa", "lsa_ng_test"), ("bert", "bert_ng_test")]:
        E = emb[key]
        results[name] = {
            **compute_participation_ratio(E),
            **compute_effective_rank(E),
            **compute_isotropy(E),
            **compute_hubness(E),
        }
        print(f"  [{name.upper()}] {results[name]}")
    return results


def run_extrinsic(emb: dict, data: dict) -> dict:
    _, _, sts_scores = data["stsb"]
    ng = data["newsgroups"]
    _, _, mrpc_labels = data["mrpc"]

    results = {}
    for name in ["lsa", "bert"]:
        sts = compute_sts(emb[f"{name}_stsb_1"], emb[f"{name}_stsb_2"], sts_scores)
        cls = compute_classification(
            emb[f"{name}_ng_train"],
            emb[f"{name}_ng_test"],
            ng["train_labels"],
            ng["test_labels"],
        )
        clu = compute_clustering(emb[f"{name}_ng_test"], ng["test_labels"])
        par = compute_paraphrase(
            emb[f"{name}_mrpc_1"], emb[f"{name}_mrpc_2"], mrpc_labels
        )
        results[name] = {**sts, **cls, **clu, **par}
        print(f"  [{name.upper()}] {results[name]}")
    return results


def lsa_sensitivity(data: dict, bert_rho: float) -> None:
    s1, s2, scores = data["stsb"]
    all_texts = list(set(s1 + s2))

    with open("../results/sensitivity.dat", "w") as f:
        f.write("k spearman\n")
        for k in [50, 100, 200, 300, 500]:
            lsa = LSAEmbedder(n_components=k)
            lsa.fit(all_texts)
            e1 = lsa.transform(s1)
            e2 = lsa.transform(s2)
            rho = compute_sts(e1, e2, scores)["spearman"]
            f.write(f"{k} {rho:.4f}\n")
            print(f"    k={k:>3d}  ρ={rho:.4f}")
        f.write(f"# BERT baseline: {bert_rho:.4f}\n")


def save_spectrum_data(emb: dict) -> None:
    lsa_sv = np.linalg.svd(emb["lsa_ng_test"], compute_uv=False)
    bert_sv = np.linalg.svd(emb["bert_ng_test"], compute_uv=False)
    lsa_sv = lsa_sv / lsa_sv[0]
    bert_sv = bert_sv / bert_sv[0]

    max_len = max(len(lsa_sv), len(bert_sv))
    with open("../results/spectrum.dat", "w") as f:
        f.write("i lsa bert\n")
        for i in range(max_len):
            l = f"{lsa_sv[i]:.6f}" if i < len(lsa_sv) else "NaN"
            b = f"{bert_sv[i]:.6f}" if i < len(bert_sv) else "NaN"
            f.write(f"{i + 1} {l} {b}\n")


def write_results_to_tex(intrinsic: dict, extrinsic: dict) -> None:
    skip = {"p_value", "optimal_threshold"}
    with open("../results/numbers.tex", "w") as f:
        for model in ["lsa", "bert"]:
            prefix = model.upper()
            for src in [intrinsic[model], extrinsic[model]]:
                for key, value in src.items():
                    if key in skip:
                        continue
                    tex_key = key.replace("_", "")
                    cmd = f"\\newcommand{{\\{prefix}{tex_key}}}{{{value:.3f}}}"
                    f.write(cmd + "\n")


def main():
    print("Loading data...")
    data = load_all()

    print("Generating embeddings...")
    emb = generate_embeddings(data)

    print("Intrinsic metrics...")
    intrinsic = run_intrinsic(emb)

    print("Extrinsic metrics...")
    extrinsic = run_extrinsic(emb, data)

    print("Spectrum...")
    save_spectrum_data(emb)

    print("LSA sensitivity...")
    bert_rho = extrinsic["bert"]["spearman"]
    lsa_sensitivity(data, bert_rho)

    print("LaTeX output...")
    write_results_to_tex(intrinsic, extrinsic)

    print("Heatmap...")
    plot_isotropy_heatmap(emb["lsa_ng_test"], emb["bert_ng_test"])

    print("Done!")


if __name__ == "__main__":
    main()
