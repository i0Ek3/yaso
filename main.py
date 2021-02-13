#!/usr/bin/env python
# coding=utf-8

import utils as u


def main():
    uncompressed = "ABBCCCDDDDEEEEEEFFFFFFFFFFFFf"
    u.compress_ratio(uncompressed)
    u.length_ratio(uncompressed)

    uncompressed = "ABCDCVCDBDADEDRTSDFLHKEDSIUILSDF"
    u.compress_ratio(uncompressed)
    u.length_ratio(uncompressed)

main()
