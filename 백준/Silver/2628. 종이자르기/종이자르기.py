x, y = map(int, input().split())
n = int(input())
y_lst = [0, y]
x_lst = [0, x]
for _ in range(n):
    d, cut = map(int, input().split())
    if d == 1:
        x_lst.append(cut)
    else:
        y_lst.append(cut)
y_lst.sort()
x_lst.sort()
cut_y = []
cut_x = []
for i in range(len(y_lst)-1):
    cut_y.append(y_lst[i+1] - y_lst[i])
for i in range(len(x_lst)-1):
    cut_x.append(x_lst[i+1] - x_lst[i])

print(max(cut_y)*max(cut_x))
