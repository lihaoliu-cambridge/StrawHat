#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from itertools import groupby

__author__ = 'LH Liu'

rows = [
    {'name': "bran", "uid": 101, "class": 13},
    {'name': "xisi", "uid": 101, "class": 11},
    {'name': "land", "uid": 103, "class": 10}
]
# data_two = sorted(rows, key=lambda x: (x["uid"], x["class"]))
# data = dict([(g, list(k)) for g, k in groupby(data_two, key=lambda x: x["uid"])])
# print(data)

dict_1 = {}
for v in rows:
    if not v.get('uid') in dict_1:
        dict_1.setdefault(v.get('uid'), [])
    dict_1[v.get('uid')].append(v)
print dict_1
