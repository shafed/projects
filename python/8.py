d = {
    "Иванов": (3, 4, 5, 4),
    "Шапаренко": (5, 5, 5, 5),
    "Пертов": (3, 3, 5, 3),
    "Лобанов": (3, 3, 3, 4),
    "Козак": (3, 4, 3, 4),
}

max_grade = max(d[i][2] for i in d)
best = []
max_sum = 0
for i in d:
    if d[i][2] == max_grade:
        best.append(i)
        max_sum = max(max_sum, sum(d[i]))

print(best)
for i in best:
    if sum(d[i]) == max_sum:
        print("best of the best:", i)
