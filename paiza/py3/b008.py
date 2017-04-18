# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

# Get input: Number of fans, number of events
# fans, events = input().split()
profit = 0


test = "".split()
# Read input:
try:
    while True:
        winloss = sum(int(i) for i in test)
        # winloss = sum(int(i) for i in input().split())
        if (winloss > 0):
            profit += winloss
        break
except:
    print(profit)
print(profit)
