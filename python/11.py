d = {"pi": 3.14, "e": 2.71, "fi": 1.62}
print(*list(i for i in d.values() if i > 2.5))
