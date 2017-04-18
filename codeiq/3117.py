# coding: utf-8

#######
# 補助関数
#######

# 整数の倍数となる、連続する2値の合計数を戻す
# ブルートフォース 全ての値を確認するため、とても遅い！
"""
def numConsecMultiples(num):
    count = 0
    # 連続する値の合計が2の倍数にならない
    if (num % 2 == 0):
        return 0
    for i in range(1, 1000001):
        if ((i*2+1) % num == 0):
            count += 1
            print(i*2+1,)
"""

# 改良Version： 範囲内の有効な倍数のみ作り出し、カウントするので早い！
"""
def numConsecMultiples(num):
    count = 0
    multiple = num
    # 連続する値の合計が2の倍数にならない
    if (num % 2 == 0):
        return 0
    else:
        while(multiple/2-1 < 1000001):
            # print(multiple)
            multiple += num*2
            count += 1
    return count
"""


# 解説Version： 数学アプローチ！
def numConsecMultiples(num):
    if (num % 2 == 0):
        return 0
    else:
        return int(int(1999999 / num) / 2.0 + 0.5)


#######
# 本題
#######

nums = []

try:
    while True:
        nums.append(int(input()))  # 標準入力

except EOFError:
    pass

for num in nums:
    print(numConsecMultiples(num))  # 結果出力
