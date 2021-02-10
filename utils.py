#!/usr/bin/env python
# coding=utf-8

import sys

import yaso


def compress_ratio(ori_str):
    ori_size = sys.getsizeof(ori_str)
    current_size = sys.getsizeof(yaso.RLE(ori_str))
    compress_ratio = current_size / ori_size

    if compress_ratio >= 1.0:
        print("Bad compress: your compress ratio is %d" % compress_ratio)
    elif 0 <= compress_ratio < 1:
        print("Good try: your compress ratio is %d" % compress_ratio)
