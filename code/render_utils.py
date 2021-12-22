# -*- coding: utf-8 -*-
# @Author: fyr91
# @Date:   2021-04-20 11:20:46
# @Last Modified by:   yirui
# @Last Modified time: 2021-12-22 12:24:59
import cv2


def get_top_left_coord(base, img,  offset_x = -4, offset_y = 0):
    w1,h1 = base.size
    w2,h2 = img.size
    x = 0
    y = 0
    x += (w1-w2)/2 + offset_x
    y += offset_y
    return int(x), int(y)


def render_tile(img_list):
    return cv2.vconcat([cv2.hconcat(img_list_h) for img_list_h in img_list])


def split_nr(files):
    norms = []
    rares = []
    for f in files:
        if '_rare' in f:
            rares.append(f)
        else:
            norms.append(f)
    return norms, rares
