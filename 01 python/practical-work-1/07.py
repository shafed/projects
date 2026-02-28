n = input("Введите последовательность: ")
cnt = 1
mx = 1
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        cnt += 1
    else:
        mx = max(cnt, mx)
        cnt = 1

mx = max(cnt, mx)
print(mx)
