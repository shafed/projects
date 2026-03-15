from datasets import load_dataset
from sklearn.datasets import fetch_20newsgroups


def load_newsgroups():
    categories = [
        "alt.atheism",
        "comp.graphics",
        "rec.sport.baseball",
        "sci.med",
        "soc.religion.christian",
        "talk.politics.guns",
    ]

    dataset = fetch_20newsgroups(
        subset="train",
        categories=categories,
        remove=("headers", "footers", "quotes"),
        random_state=42,
    )
    return (dataset.data, dataset.target)


def load_stsb():
    dataset = load_dataset("sentence-transformers/stsb", split="train")
    return (
        list(dataset["sentence1"]),
        list(dataset["sentence2"]),
        list(dataset["score"]),
    )


def load_mrpc():
    dataset = load_dataset("glue", "mrpc", split="train")
    return (
        list(dataset["sentence1"]),
        list(dataset["sentence2"]),
        list(dataset["label"]),
    )


def load_all():
    return {"newsgroups": load_newsgroups(), "stsb": load_stsb(), "mrpc": load_mrpc()}
