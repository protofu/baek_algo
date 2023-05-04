word = input()
lst = [0]*26
for w in word:
    lst[ord(w)-97] += 1

print(*lst)
