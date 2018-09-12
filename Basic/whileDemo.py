# -*- coding: UTF-8 -*-
import random

num = random.randint(1, 100)
count = 0
while count < 3:
    num1 = input("请输入猜数")
    num1 = int(num1)
    if num1 > num:
        print("太大了")
    elif num1 < num:
        print("太小了")
    elif num1 == num:
        print("猜对了！")
        break
    count += 1
else:
    print("次数用完了，请重新开始游戏")