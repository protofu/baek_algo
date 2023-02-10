n, m = input().split()

num_list = list(map(int, input().split()))

num_list.sort()

print(num_list[int(n)-int(m)])