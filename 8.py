S = 0
N = 0
for i in range(int(1000000)):
    r1 = i % 10
    r2 = (i % 100) // 10
    r3 = (i%1000)//100
    l1 = i // 100000
    l2 = (i % 100000) // 10000
    l3 = (i % 10000) // 1000

    if r1 + r2 + r3 == l1 + l2 + l3:
        S += 1
        if l1 + l2 + l3 == 13:
            N += 1


print(f'{S} - кол-во счастливых билетов')
print(f'{N} - кол-во счастливых билетов с суммой 13')
