#!usr/bin/env python3
# -*- coding : utf-8 -*-

t = ()
print(len(t))

t = (1,)
print(type(t))
print(t)

t = ('a', 'b', ['A', 'B'])
print(t[2][0])
print(t[2][1])
print(t)

t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
