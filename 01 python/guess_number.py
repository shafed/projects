import random

n = random.randint(1, 100)
cnt = 0
while True:
    try:
        x = int(input("Твоя попытка: "))
        cnt += 1
        if x > n:
            print("Меньше!")
            cnt += 1
            continue
        elif x < n:
            print("Больше!")
            cnt += 1
            continue
        if x == n:
            print("Правильно!")
            print(f"Ты угадал за {cnt} попыток!")
            break
    except ValueError:
        print("Это не число")
