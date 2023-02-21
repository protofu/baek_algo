n =int(input())
num = []
for _ in range(n):
    num += list(map(int, input().split()))
    num = sorted(num, reverse=True)[:n]
print(num[-1])