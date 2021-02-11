#!/usr/bin/env python
# coding=utf-8

import yaso
import utils as u


def main():
    uncompressed = "ABBCCCDDDD"
    u.compress_ratio(uncompressed)
    u.length_ration(uncompressed)

    uncompressed = "ABCDCVCDBDADEDRT"
    u.compress_ratio(uncompressed)
    u.length_ration(uncompressed)

main()
