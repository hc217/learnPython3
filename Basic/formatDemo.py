#!usr/bin/env python3
# -*- coding: UTF-8 -*-

print("hello %s" % "world")
# 字符串使用 %s
print("hi %s , your have $%d" % ('sindy', 100000))
# 整数使用%d
print("growth rate %d%%" % 7)
# 需要使用百分号时使用两个来标示
print("%.2f" % 3.1415926)

s1 = 72
s2 = 85
rate = (s2/s1-1)*100
print("小明的成绩提高了 %.2f%%" % rate)
print("小明的成绩提高了 {0:.2f}%".format(rate))

