N = int(input("N = "))
K = int(input("K = "))
S = 0
for i in range(N, K+1):
    S += i
print(f'{S} - сумма чисел между N и K')