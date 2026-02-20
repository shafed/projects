d = {"1": 1.29, "2": 0.43}
temp = {"3": d["1"] * d["2"]}
d.update(temp)
print(d)
