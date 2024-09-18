x = int(input("x = "))
N = int(input("N = "))
S = 0
for i in range(1, N + 1):
    S += 1 / (x**(2*i-2))
print (S)