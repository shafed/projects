n = int(input("Введите число карточек: "))
# ttl = sum(i for i in range(1, n + 1))
ttl = (1 + n) * n // 2  # арифметическая прогрессия
for i in range(n - 1):
    x = int(input("Введите номер карточки: "))
    ttl -= x
print(ttl)
