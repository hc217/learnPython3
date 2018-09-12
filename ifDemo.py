#!usr/bin/env python3
# -*- coding: utf-8 -*-

height = 1.75
weight = 79.5

bmi = weight/height**2

if bmi < 18.5:
    print("体重过轻")
elif 25 <= bmi <= 28:
    print("体重过重")
elif 28<= bmi <= 32:
    print("肥胖")
elif bmi > 32:
    print("严重肥胖")
else:
    print("正常")