
era = [0, 0] + [i for i in range(2, 10001)]
for i in range(2, int((10000)**0.5)):
    for j in range(i+i, len(era), i):
        era[j] = 0

n = int(input())
for _ in range(n):
    num = int(input())

    for i in range(10000):
        if era[num//2 + i] + era[num//2 - i] == num:
            print(era[num//2 - i], era[num//2 + i])
            break