a,b=map(int,input().split())
cards = list(map(int,input().split()))
sum_=[]
last_sum=[]
for i in cards:
    for j in range(cards.index(i)+1,a):
        for k in range(j+1,a):
            sum_.append(i+cards[j]+cards[k])
for i in sum_:
    if i<=b:
        last_sum.append(i)           
print(max(last_sum))