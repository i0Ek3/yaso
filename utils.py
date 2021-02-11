#!/usr/bin/env python
# coding=utf-8

import sys

import yaso


def compress_ratio(ori_str):
    ori_size = sys.getsizeof(ori_str)
    cur_size = sys.getsizeof(yaso.RLE(ori_str))
    compress_ratio = cur_size / ori_size
    threshold = 0.8

    if compress_ratio >= threshold:
        print("Bad compress: your compress ratio is %d" % compress_ratio)
    elif 0 <= compress_ratio < threshold:
        print("Good try: your compress ratio is %d" % compress_ratio)

def length_ration(ori_str):
    ori_len = len(ori_str)
    cur_len = len(yaso.RLE(ori_str))
    len_ratio = cur_len / ori_len

    if len_ratio >= threshold:
        print("Bad!")
    else:
        print("Good!")
