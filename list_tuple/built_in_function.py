# 列表和元组常用的内置函数：

l = [3, 2, 3, 7, 8, 1]
print(l.count(3))  # count(item) 表示统计列表 item 出现的次数。
# 2
print(l.index(7))  # index(item) 表示返回列表 item 第一次出现的索引。
# 3
l.reverse()
print(l)  # reverse() 原地倒转列表
# [1, 8, 7, 3, 2, 3]
l.sort()
print(l)     # sort() 对列表排序
# [1, 2, 3, 3, 7, 8]

l.append(99)
print(l)     # append（）在列表尾部增加一个内容
# [1, 2, 3, 3, 7, 8, 99]

l.remove(99)
print(l)  # remove()删除内容
# [1, 2, 3, 3, 7, 8]

a = l.copy()
print(a)  # copy()将列表的值复制给一个新列表
# [1, 2, 3, 3, 7, 8]

l.clear()
print(l)  # clear()将列表清空
# []

l = [1, 2, 3, 3, 7, 8]

l1 = [11, 12, 13]
l.extend(l1)  # extend() 在列表后增加另一个列表，等同与 l+l1
print(l)
# [1, 2, 3, 3, 7, 8, 11, 12, 13]

l.insert(6,9)
print(l)  # insert()在角标位置插入一个内容
# [1, 2, 3, 3, 7, 8, 9, 11, 12, 13]

del l[0:6]
print(l)  # del删除列表指定位置的内容
# [9, 11, 12, 13]

l.pop(1)
print(l)  # pop()返回角标值并删掉
# [9, 12, 13]

tup = (3, 2, 3, 7, 8, 1) #
print(tup.count(3))  # count(item) 表示统计元组 item 出现的次数。
# 2
print(tup.index(7))  # index(item) 表示返回元组 item 第一次出现的索引。
# 3
print(list(reversed(tup)))  # 返回一个倒转的迭代器，需要用list()转换才能输出
# [1, 8, 7, 3, 2, 3]
print(sorted(tup))  #  返回一个排序后的列表
# [1, 2, 3, 3, 7, 8]