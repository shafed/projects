# while n:
#     sum += n
#     n = int(input("Введите число: "))

ttl = 0
while True:
    n = int(input("Введите число: "))
    if n == 0:
        break
    ttl += n
print(ttl)
