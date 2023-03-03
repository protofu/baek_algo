import sys
sys.setrecursionlimit(501)

def fac(n):
    if n == 1:
        return 1
    return fac(n-1) * n
num = int(input())
if num == 0:
    print(0)
else:
    num = str(fac(num))

    n = 1
    while not int(num[-n]):
        n += 1

    print(n-1)