#!/usr/bin/env python
# coding=utf-8

import sys

import RLE as rle


threshold = 1.0
mininum = 0.001

def compress_ratio(ori_str):
    ori_size = sys.getsizeof(ori_str)
    cur_size = sys.getsizeof(rle.RLE(ori_str))
    compress_ratio = (cur_size + mininum) / (ori_size + mininum)

    if compress_ratio >= threshold:
        print("Bad compress: your compress ratio is %d" % compress_ratio)
    else:
        print("Good try: your compress ratio is %d" % compress_ratio)

def length_ratio(ori_str):
    ori_len = len(ori_str)
    cur_len = len(rle.RLE(ori_str))
    len_ratio = (cur_len + mininum) / (ori_len + mininum)

    if len_ratio >= threshold:
        print("Bad: your length ratio is %d" % len_ratio)
    else:
        print("Good: your length ratio is %d" % len_ratio) 
