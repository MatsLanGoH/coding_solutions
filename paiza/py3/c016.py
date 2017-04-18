# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import re

p = re.compile('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')

tries = input()

try:
    while True:
        line_input = input()
        if (p.match(line_input)):
            print(True)
        else:
            print(False)
except:
    pass
