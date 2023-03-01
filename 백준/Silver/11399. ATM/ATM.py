n = int(input())
lst = list(map(int, input().split()))
time = 0
lst.sort()

for i in range(n):
    for j in range(i+1):
        time += lst[j]
print(time)