getMoney = 1000 - int(input())
coin = 0
if getMoney >= 500:
    coin += getMoney//500
    getMoney %= 500

if getMoney >= 100:
    coin += getMoney//100
    getMoney %= 100

if getMoney >= 50:
    coin += getMoney//50
    getMoney %= 50

if getMoney >= 10:
    coin += getMoney//10
    getMoney %= 10

if getMoney >= 5:
    coin += getMoney//5
    getMoney %= 5

if getMoney >= 1:
    coin += getMoney//1
    getMoney %= 1
    
print(coin)