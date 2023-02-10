n = int(input())
words = []
for _ in range(n):
    words.append(input())
word_list = []
for word in words:
    if word not in word_list:
        word_list.append(word)
word_list.sort()
word_list.sort(key=len)

for i in word_list:
    print(i)