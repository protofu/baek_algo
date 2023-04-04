n = int(input())
w = input()
cnt = 0
lst = ['a', 'e', 'i', 'o', 'u']
for i in w:
    if i in lst:
        cnt += 1
print(cnt)