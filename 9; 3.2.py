#3.2
stipendia = int(input("Сколько мама на обеды дает? "))
rashodi = int(input("Введите коэффицент транжирства в месяц: "))
months = int(input("Сколько месяцев будешь кошмарить деньги? "))
sum = 0
min = 0
if stipendia < rashodi:
        for i in range(1, months+1):
            if i % 2 == 1:
                rashodi *= 1.03
            else:
                rashodi *= 1.05
            sum += stipendia
            min += rashodi
        print(f'{min - sum} - начальная сумма для выживания')
else:
    print("Живи, кайфуй")