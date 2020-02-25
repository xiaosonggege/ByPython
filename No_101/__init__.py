#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: __init__.py
@time: 2020/2/23 10:18 上午
'''
from collections import namedtuple
import copy

class BiTreeProperty:
    def __init__(self, name):
        self._name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class BiTreesProperty:
    def __init__(self, name):
        self._name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value:tuple):
        value = list(value)
        stack = []
        stack.append(instance.__dict__[self._name])
        BiTreesProperty.build(value, stack)

    @staticmethod
    def build(value, stack):
        # stack[0].data = value.pop(0)
        if len(value):
            stack[0].data = value.pop(0)
            if len(value) > len(stack[1:]):
                stack[0].lchild = BiTree()
                stack.append(stack[0].lchild)
            if len(value) > len(stack[1:]):
                stack[0].rchild = BiTree()
                stack.append(stack[0].rchild)
            stack.pop(0)
            BiTreesProperty.build(value, stack)

class BiTree:
    def __init__(self, data=0, lchild=None, rchild=None):
        self._data = data
        self._lchild = lchild
        self._rchild = rchild

    data = BiTreeProperty('data')
    lchild = BiTreeProperty('lchild')
    rchild = BiTreeProperty('rchild')

class BiTrees:
    root = BiTreesProperty('root')
    def __init__(self):
        self._root = BiTree()
    def __call__(self, *args, **kwargs):
        self.root = args
        return self.root

if __name__ == '__main__':
    tree = BiTrees()
    lis = [1, 2, 2, 3, 4, 4, 3]
    root = tree(*lis)
    print('root')

