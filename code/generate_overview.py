# -*- coding: utf-8 -*-
# @Author: yirui
# @Date:   2021-12-22 12:06:38
# @Last Modified by:   yirui
# @Last Modified time: 2021-12-22 12:14:40
import os
import cv2
from config import *
from render_utils import *

root = "../res/individuals"
generated_imgs = []
for i in range(ROWS*COLS):
    generated_imgs.append(cv2.resize(cv2.imread(os.path.join(root, f"#{i}.png")), OVERVIEW_UNIT_SIZE))

img_tile = [generated_imgs[i * COLS:(i + 1) * COLS] for i in range(ROWS)]
res = render_tile(img_tile)
cv2.imwrite('../res/overview.png', res)

