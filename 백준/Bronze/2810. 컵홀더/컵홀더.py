n = int(input())
seat = list(input())
person = len(seat)
cup = ['*']
while seat:
    a = seat.pop(0)
    if a == 'S':
        cup.append('*')
    elif a == 'L' and cup[-1] == 'L':
        cup.pop()
        cup.append('*')
    else:
        cup.append(a)
b = len(cup)
if n > b:
    print(b)
else:
    print(n)