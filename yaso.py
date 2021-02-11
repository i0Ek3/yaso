#!/usr/bin/env python
# coding=utf-8
    
import collections


def RLE(ori_str):
    count_dict = collections.OrderedDict.fromkeys(ori_str, 0)
    for c in ori_str:
       count_dict[c] += 1

    encoded_str = ""
    for key, value in count_dict.items():
       encoded_str += key + str(value)

    return encoded_str
