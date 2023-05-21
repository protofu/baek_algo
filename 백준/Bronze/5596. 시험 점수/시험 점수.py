score1 = sum(list(map(int, input().split())))
score2 = sum(list(map(int, input().split())))
print(score1 if score2 < score1 else score2)