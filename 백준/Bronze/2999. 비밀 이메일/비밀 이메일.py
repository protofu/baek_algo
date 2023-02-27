pw = input()
n = len(pw)
word = ''
for i in range(1, int(n**0.5)+1):
    if not n%i:
        r = i
        c = n//i

lst = [[0] * c for _ in range(r)]
cnt = 0
for y in range(c):
    for x in range(r):
        lst[x][y] = pw[cnt]
        cnt += 1

for y in range(r):
    for x in range(c):
        word += lst[y][x]
print(word)