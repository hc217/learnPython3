# -*- coding: UTF-8 -*-
import random

sum01 = 0
for i in range(1, 101):
    sum01 = sum01 + i
print(sum01)

num = random.randint(1, 100)
for i in range(3):
    num1 = input("请输入猜测的数字")
    num1 = int(num1)
    if num1 > num:
        print("太大了")

    elif num1 < num:
        print("太小了")

    elif num1 == num:
        print("恭喜你，猜对了！")

else:
    print("次数用尽，请重新开始")

