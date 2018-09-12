#!usr/bin/env python3
# -*- coding: UTF-8 -*-

listEmpty = []
print(len(listEmpty))
# 空列表

colleague = ['JX', 'WQ', 'HF']
print(colleague[0])
# 通过索引定位列表元素

colleague.append('PH')
print(colleague)
# 在列表末尾增加一个元素

colleague.pop(3)
print(colleague)
# 通过索引删除一个元素

colleague.insert(1, 'LW')
print(colleague)
# 将元素插入指定索引的位置

colleague[1] = 'PH'
print(colleague)
# 通过索引对列表元素重新赋值

appTeam = ['DD', 'ZR']
colleague.insert(2, appTeam)
print(colleague)
# 将一个列表插入另一个列表

print(colleague[2][0])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
# 打印Apple

print(L[1][1])
# 打印Python

print(L[2][2])
# 打印Lisa

for name in colleague:
    print(name)
