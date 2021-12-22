# -*- coding: utf-8 -*-
# @Author: yirui
# @Date:   2021-12-22 12:06:38
# @Last Modified by:   fyr91
# @Last Modified time: 2021-12-23 00:24:10
import os
import cv2
from config import *
from render_utils import *

root = "../res/individuals"
generated_imgs = []
for i in range(ROWS * COLS):
    print(f"processing {i+1}", end="\r", flush=True)
    file_path = os.path.join(root, f"#{i+1}.png")
    # print(file_path)
    img = cv2.imread(file_path)
    # print(img)
    generated_imgs.append(cv2.resize(img, OVERVIEW_UNIT_SIZE))

img_tile = [generated_imgs[i * COLS:(i + 1) * COLS] for i in range(ROWS)]
res = render_tile(img_tile)
cv2.imwrite('../res/overview.png', res)
