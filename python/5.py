s = 1000
y = int(input())
n = 1.01
for year in range(1, y+1):
    for month in range(12):
        s *= n
    n += 0.001
print(s)


