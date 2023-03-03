import sys
input = sys.stdin.readline

n = int(input())
S = []
for _ in range(n):
    word = list(map(str, input().split()))
    if len(word) == 2:
        num = int(word[1])
    if word[0] == 'add':
        if num not in S:
            S.append(num)
    elif word[0] == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif word[0] == 'remove':
        if num in S:
            S.remove(num)
    elif word[0] == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.append(num)
    elif word[0] == 'empty':
        S = []
    elif word[0] == 'all':
        S = [i for i in range(1, 21)]