# -*- coding: utf-8 -*-
# @Author: User
# @Date:   2021-04-16 11:05:13
# @Last Modified by:   fyr91
# @Last Modified time: 2021-12-22 00:50:12
import cv2
from PIL import Image
import os
from os import path as osp
import numpy as np
import random
from render_utils import *
from config import *

num_rare_items = 0
num_rare1 = 0
num_rare2 = 0
num_rare3 = 0
num_normal = 0
existing_designs = []

_, _, tops = next(os.walk(TOP_DIR))
_, _, glasses = next(os.walk(GLASSES_DIR))
_, _, hands = next(os.walk(HAND_DIR))

normal_tops, rare_tops = split_nr(tops)
normal_glasses, rare_glasses = split_nr(glasses)
normal_hands, rare_hands = split_nr(hands)

rows = 20
cols = 40
unit_size = (148, 148)
generated_imgs = []

while len(generated_imgs) < rows * cols:

    # init and create empty final render
    got_rare = False
    render = Image.new('RGB', (592, 592))

    # select body type & color
    body_type = random.choice(BODY_TYPES)
    # body_type = 'pd_04'
    # body_color_prob = random.random()
    # if body_color_prob > 0 and body_color_prob <= 0.1:
    #     body_color = 'blue'
    # elif body_color_prob <= 0.2:
    #     body_color = 'red'
    # elif body_color_prob <= 0.3:
    #     body_color = 'green'
    # elif body_color_prob <= 0.4:
    #     body_color = 'purple'
    # elif body_color_prob <= 0.5:
    #     body_color = 'brown'
    # else:
    #     body_color = 'black'

    body_color = "black"

    # determine accessories
    got_top = random.random() < TOP_PROB
    got_glasses = random.random() < GLASSES_PROB
    got_right_hand = random.random() < RIGHT_HAND_PROB
    got_left_hand = random.random() < LEFT_HAND_PROB

    rare_number = 0

    if got_top:
        if random.random() < RARE_PROB:
            got_rare = True
            rare_number += 1
            top_file = random.choice(rare_tops)
        else:
            top_file = random.choice(normal_tops)
    else:
        top_file = ''

    if got_glasses:
        if random.random() < RARE_PROB:
            got_rare = True
            rare_number += 1
            glasses_file = random.choice(rare_glasses)
        else:
            glasses_file = random.choice(normal_glasses)
    else:
        glasses_file = ''

    if got_right_hand:
        if random.random() < RARE_PROB:
            got_rare = True
            rare_number += 1
            right_hand_file = random.choice(rare_hands)
        else:
            right_hand_file = random.choice(normal_hands)
    else:
        right_hand_file = ''

    if got_left_hand and not got_right_hand:
        if random.random() < RARE_PROB:
            got_rare = True
            rare_number += 1
            left_hand_file = random.choice(rare_hands)
        else:
            left_hand_file = random.choice(normal_hands)
        # # only allow one bag & one phone on hand
        # if ('bag' in right_hand_file and 'bag' in left_hand_file) or ('phone' in right_hand_file and 'phone' in left_hand_file):
        #     left_hand_file = ''
    else:
        left_hand_file = ''

    design = []
    design.append(body_type)
    design.append(body_color)
    design.append(top_file)
    design.append(glasses_file)
    design.append(right_hand_file)
    design.append(left_hand_file)
    design_str = ",".join(design)
    if (design_str in existing_designs) or "disabled" in design:
        continue
    else:
        existing_designs.append(design_str)
        print(f'generated {len(existing_designs)}/{rows*cols} unique designs', end="\r", flush=True)

    # select bg files
    bg_file = random.choice(BG_FILES)

    # change body color if got rare
    # change bg if got rare
    if rare_number == 3:
        body_color = "gold"
        bg_file = RARE_BG_FILES[2]
        num_rare3 += 1
    elif rare_number == 2:
        body_color = "silver"
        bg_file = RARE_BG_FILES[1]
        num_rare2 += 1
    elif rare_number == 1:
        body_color = "bronze"
        bg_file = RARE_BG_FILES[0]
        num_rare1 += 1
    else:
        body_color = "black"
        num_normal += 1

    bg = Image.open(f'../assets/bg/{bg_file}')

    render.paste(bg, (0, 0))
    body = Image.open(f'../assets/base/{body_type}/{body_color}.png')
    render.paste(body, (0, 0), body)
    if got_top:
        top_path = osp.join(TOP_DIR, top_file)
        accessory = Image.open(top_path)
        x, y = get_top_left_coord(render, accessory, OFFSET[body_type]["top"][0], OFFSET[body_type]["top"][1])
        render.paste(accessory, (x, y), accessory)
    if got_glasses:
        glasses_path = osp.join(GLASSES_DIR, glasses_file)
        accessory = Image.open(glasses_path)
        x, y = get_top_left_coord(render, accessory, OFFSET[body_type]["glasses"][0], OFFSET[body_type]["glasses"][1])
        render.paste(accessory, (x, y), accessory)
    if got_right_hand and right_hand_file != '':
        right_hand_path = osp.join(HAND_DIR, right_hand_file)
        accessory = Image.open(right_hand_path)
        x, y = get_top_left_coord(render, accessory, OFFSET[body_type]["right_hand"][0], OFFSET[body_type]["right_hand"][1])
        render.paste(accessory, (x, y), accessory)
    if got_left_hand and left_hand_file != '':
        left_hand_path = osp.join(HAND_DIR, left_hand_file)
        accessory = Image.open(left_hand_path)
        accessory = accessory.transpose(Image.FLIP_LEFT_RIGHT)
        x, y = get_top_left_coord(render, accessory, OFFSET[body_type]["left_hand"][0], OFFSET[body_type]["left_hand"][1])
        render.paste(accessory, (x, y), accessory)

    # cvt to cv2 and resize
    cv2_img = np.array(render)
    cv2_img = cv2_img[:, :, ::-1].copy()
    cv2_img = cv2.resize(cv2_img, unit_size)
    generated_imgs.append(cv2_img)


# generate image grid
img_tile = [generated_imgs[i * cols:(i + 1) * cols] for i in range(rows)]
res = render_tile(img_tile)

# cv2.imshow('overlay', res)
# cv2.waitKey(0)
# # if cv2.waitKey(0) & 0xFF == ord('q'):
# #     break
#     #closing all open windows
# cv2.destroyAllWindows()

# write to file
cv2.imwrite('../res/result_test.png', res)
# print(f"\n{num_rare_items} rare items created")
print(f"""
Summary:\n
  {num_normal} normal pandas generated\n
  {num_rare1} rare level 1 pandas generated\n
  {num_rare2} rare level 2 pandas generated\n
  {num_rare3} rare level 3 pandas generated\n
    """)
