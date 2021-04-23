# -*- coding: utf-8 -*-
# @Author: User
# @Date:   2021-04-21 14:26:54
# @Last Modified by:   fyr91
# @Last Modified time: 2021-04-21 14:39:13
import cv2
from PIL import Image
import os
from os import path as osp
import numpy as np
import random
from render_utils import *
from config import *


bg_color = (253, 249, 241)
body_type = 'pd_04'
body_color = 'black'
top_file = 'rare_20.png'
glasses_file = 'gls_04.png'
output = 'tall.png'

top_path = osp.join(TOP_DIR, top_file)
glasses_path = osp.join(GLASSES_DIR, glasses_file)

render = Image.new('RGB', (600,600))
bg = Image.new('RGB', (600, 600), bg_color)
render.paste(bg, (0,0))

body = Image.open(f'../assets/base/{body_type}/{body_color}.png')
render.paste(body, (0,0), body)

# top
accessory = Image.open(top_path)
x, y = get_top_left_coord(render, accessory, OFFSET[body_type]["top"][0], OFFSET[body_type]["top"][1])
render.paste(accessory, (x,y), accessory)

# glasses
accessory = Image.open(glasses_path)
x, y = get_top_left_coord(render, accessory, OFFSET[body_type]["glasses"][0],  OFFSET[body_type]["glasses"][1])
render.paste(accessory, (x,y), accessory)

render.save(f'../res/{output}')
