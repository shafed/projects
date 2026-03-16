import numpy as np
from datasets import load_dataset
from sklearn.datasets import fetch_20newsgroups

CATEGORIES = [
    "alt.atheism",
    "comp.graphics",
    "rec.sport.baseball",
    "sci.med",
    "soc.religion.christian",
    "talk.politics.guns",
]


def load_newsgroups():
    kw = dict(
        categories=CATEGORIES,
        remove=("headers", "footers", "quotes"),
        random_state=42,
    )
    train = fetch_20newsgroups(subset="train", **kw)
    test = fetch_20newsgroups(subset="test", **kw)

    def _filter(bunch):
        mask = [i for i, t in enumerate(bunch.data) if len(t.strip()) > 10]
        bunch.data = [bunch.data[i] for i in mask]
        bunch.target = bunch.target[mask]
        return bunch

    train, test = _filter(train), _filter(test)
    return {
        "train_texts": train.data,
        "train_labels": train.target,
        "test_texts": test.data,
        "test_labels": test.target,
    }


def load_stsb():
    dataset = load_dataset("sentence-transformers/stsb", split="test")
    return (
        list(dataset["sentence1"]),
        list(dataset["sentence2"]),
        list(dataset["score"]),
    )


def load_mrpc():
    dataset = load_dataset("glue", "mrpc", split="validation")
    return (
        list(dataset["sentence1"]),
        list(dataset["sentence2"]),
        list(dataset["label"]),
    )


def load_all():
    return {
        "newsgroups": load_newsgroups(),
        "stsb": load_stsb(),
        "mrpc": load_mrpc(),
    }
