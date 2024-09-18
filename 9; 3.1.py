#3.1
stipendia = int(input("Сколько мама на обеды дает? "))
rashodi = int(input("Введите коэффицент транжирства в месяц: "))
months = int(input("Сколько месяцев будешь кошмарить деньги? "))
sum = 0
min = 0
if stipendia < rashodi:
        for i in range(1, months+1):
            sum += stipendia
            min += rashodi
        print(f'{min - sum} - начальная сумма для выживания')
else:
    print("Живи, кайфуй")





