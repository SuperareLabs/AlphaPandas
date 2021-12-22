# -*- coding: utf-8 -*-
# @Author: User
# @Date:   2021-04-21 14:26:54
# @Last Modified by:   fyr91
# @Last Modified time: 2021-12-22 22:51:24
import cv2
from PIL import Image
import os
from os import path as osp
import numpy as np
import random
from render_utils import *
from config import *

rares = [
	['pd_01','gold,demon_horns_gold_rare.png','gls_stylish_green_rare.png','bitcoin_rare.png'],
    ['pd_02','gold,flowerhat_rainbow_rare.png','gls_futuristic_purple_rare.png','windmill_colorful_rare.png'],
    ['pd_03','gold,crown_special_rare.png','gls_stylish_yellow_rare.png','handbag_pink_rare.png'],
    ['pd_04','gold,octopus_hat_red_rare.png','gls_butterfly_rare.png','skeleton_head_gray_rare.png']
]


body_type = 'pd_03'
body_color = 'gold'
head_file = 'crown_special_rare.png'
glasses_file = 'gls_stylish_yellow_rare.png'
hand_file = 'handbag_pink_rare.png'

output = '#1330.png'

head_path = osp.join(HEADS_DIR, head_file)
glasses_path = osp.join(GLASSES_DIR, glasses_file)
hand_path = osp.join(HAND_DIR, hand_file)

bg_file = RARE_BG_FILES[2]
bg = Image.open(f'../assets/bg/{bg_file}')
# bg = Image.new('RGB', (592, 592), bg_color)
render = Image.new('RGB', (592, 592))
render.paste(bg, (0, 0))

body = Image.open(f'../assets/base/{body_type}/{body_color}.png')
render.paste(body, (0, 0), body)

# top
accessory = Image.open(head_path)
x, y = get_top_left_coord(render, accessory, OFFSET[body_type]["head"][0], OFFSET[body_type]["head"][1])
render.paste(accessory, (x, y), accessory)

# glasses
accessory = Image.open(glasses_path)
x, y = get_top_left_coord(render, accessory, OFFSET[body_type]["glasses"][0], OFFSET[body_type]["glasses"][1])
render.paste(accessory, (x, y), accessory)

# right hand
accessory = Image.open(hand_path)
x, y = get_top_left_coord(render, accessory, OFFSET[body_type]["right_hand"][0], OFFSET[body_type]["right_hand"][1])
render.paste(accessory, (x, y), accessory)

render.save(f'../res/{output}')
