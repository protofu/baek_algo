import sys
import math

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


def sum_f(x):
    if x <= 0:
        return 0

    seung = int(math.log2(x))
    floor_2pow = 2 ** seung
    if floor_2pow == x:
        return seung * x // 2 + 1

    diff = x - floor_2pow
    return sum_f(floor_2pow) + diff + sum_f(diff)


a, b = map(int, input().split())
print(sum_f(b) - sum_f(a - 1))