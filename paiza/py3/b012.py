# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

tries = input()


def digitChecker(number):
    checkSum = ""

    for idx, digit in enumerate(number):
        if idx % 2 == 1:
            checkSum += digit
        else:
            checkSum += str(int(digit) * 2)
    total = sum([int(i) for i in checkSum])

    checkDigit = 10 - total % 10

    if checkDigit < 10:
        return checkDigit
    else:
        return 0

try:
    while True:
        line_input = input()
        print(digitChecker(line_input[:-1]))
except:
    pass
