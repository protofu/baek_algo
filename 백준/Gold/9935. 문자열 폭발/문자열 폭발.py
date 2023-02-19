st = input()
boom = list(input())
stk = []


for s in st:
    stk.append(s)

    if s == boom[-1] and len(stk) >= len(boom):
        if stk[len(stk)-len(boom):len(stk)] == boom:
            for _ in range(len(boom)):
                stk.pop()
if stk:
    print(*stk, sep='')
else:
    print('FRULA')