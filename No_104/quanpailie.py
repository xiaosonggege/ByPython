#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: quanpailie
@time: 2020/2/28 2:10 下午
'''

class Aproperty:
    def __init__(self, name):
        self._name = '_' + name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class A:
    """全排列"""
    def __init__(self, lis=None):
        self._list = lis
        self._result = []
    lis = Aproperty('list')
    low = 0
    def _quanpailie(self, lis, index=0):
        for i in range(0, len(lis)):
            lis[0], lis[i] = lis[i], lis[0]
            if A.low != len(self._list)-1:
                A.low += 1
                self._quanpailie(lis, index=A.low)
            else:
                self._result.append(lis)
            lis[0], lis[i] = lis[i], lis[0]
            A.low = 0
    def __call__(self, *args, **kwargs):
        self._quanpailie(self._list)
        return self._result

if __name__ == '__main__':
    l = [1, 2, 3]
    a = A(l)
    for i in a():
        print(i)