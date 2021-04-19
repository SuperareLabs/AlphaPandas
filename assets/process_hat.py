# -*- coding: utf-8 -*-
# @Author: fyr91
# @Date:   2021-04-19 18:41:57
# @Last Modified by:   fyr91
# @Last Modified time: 2021-04-19 18:44:26
import cv2
import os

files = [f for f in os.listdir('hat') if 'png' in f]
print(files)

for f in files:
    path = os.path.join('hat', f)
    img = cv2.imread(path, -1)
    img = img[16:-1,:]
    cv2.imwrite(f'hat2/{f}', img)
