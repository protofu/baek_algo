import sys
input = sys.stdin.readline

n, m = map(int,input().split())
tree =list(map(int, input().split()))

sear = 0
end = max(tree)
while sear<=end:
    half = (sear + end) // 2
    height = 0
    for tre in tree:
        if tre - half >=0:
            height += tre - half
    if height >= m:
        sear = half + 1
    else:
        end = half - 1
print(end)