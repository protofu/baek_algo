word = input()
cnt = 0
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for _ in range(len(word)):
    for i in cro:
        if i in word:
            word=word.replace(i,'0')
             
cnt+=len(word)            
print(cnt)
    