n = int(input())
lst = list(map(int, input().split()))
stk = []
for i in range(1, n+1):
    stk.insert(lst[i-1],i)
print(*stk[::-1])