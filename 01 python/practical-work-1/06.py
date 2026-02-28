n = int(input())
if 11 <= n % 100 <= 14:
    print(f"{n} Коров")
elif n % 10 == 1:
    print(f"{n} Корова")
elif n % 10 in (2, 3, 4):
    print(f"{n} Коровы")
else:
    print(f"{n} Коров")
