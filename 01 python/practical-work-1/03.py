n = int(input("Введите число минут: "))
# print(n // 60 % 24, ":", n % 60, sep="")
# print(f"{n // 60 % 24}:{'00' if n % 60 == 0 else n % 60}")
print(f"{n // 60 % 24}:{n % 60:02d}")
