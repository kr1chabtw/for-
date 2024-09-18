N = int(input("N = "))
K = int(input("K = "))
S = 0
for i in range(N, K+1):
    if i % 2 == 0:
        S += i
print(f'{S} - сумма четных чисел между N и K')