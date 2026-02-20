d = {1: 1, "2": 2, "3": 3, 4: 4}
m = d.copy()
for i in d.keys():
    if i is str:
        m.pop(i)
print(m)
