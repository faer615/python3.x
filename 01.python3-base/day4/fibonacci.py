#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh
# 斐波那契数列 生成器

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b  # yield 生成器
        a,b = b, a + b
        n = n + 1
    return '--- done ---'

#f = fib(10)
g = fib(10)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break