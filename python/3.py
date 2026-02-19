passwd = input()
if len(passwd) != 4:
    print("Пароль не состоит из 4 разрядов")
    exit()
for i in range(10000):
    j = str(i)
    if i < 1000:
        j = "0" * (4 - len(j)) + j
    if passwd == j:
        print("Пароль найден!", passwd)
