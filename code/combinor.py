# -*- coding: utf-8 -*-
# @Author: User
# @Date:   2021-04-16 11:05:13
# @Last Modified by:   fyr91
# @Last Modified time: 2021-04-20 11:32:59
import cv2
from PIL import Image
import os
from os import path as osp
import numpy as np
import random
from render_utils import *

if __name__ == '__main__':
    from config import *

    existing_designs = []

    _,_,tops = next(os.walk(TOP_DIR))
    _,_,glasses = next(os.walk(GLASSES_DIR))

    normal_tops, rare_tops = split_nr(tops)
    normal_glasses, rare_glasses = split_nr(glasses)

    rows = 15
    cols = 30
    unit_size = (120,120)
    generated_imgs = []

    while len(generated_imgs) < rows*cols:

        # create empty final render
        render = Image.new('RGB', (600,600))


        # select bg and render
        bg_color = random.choice(BG_COLORS)
        bg = Image.new('RGB', (600, 600), bg_color)
        render.paste(bg, (0,0))


        # select body type & color
        body_type = random.choice(BODY_TYPES)
        body_color_prob = random.random()
        if body_color_prob > 0 and body_color_prob <= 0.1:
            body_color = 'blue'
        elif body_color_prob <= 0.2:
            body_color = 'red'
        elif body_color_prob <= 0.3:
            body_color = 'green'
        elif body_color_prob <= 0.4:
            body_color = 'purple'
        elif body_color_prob <= 0.5:
            body_color = 'brown'
        else:
            body_color = 'black'


        # render selected body with bg
        body = Image.open(f'../assets/base/{body_type}/{body_color}.png')
        render.paste(body, (0,0), body)


        # determine accessories
        got_top = random.random()<TOP_PROB
        got_glasses = random.random()<GLASSES_PROB

        if got_top:
            if random.random() < RARE_PROB:
                top_file = random.choice(rare_tops)
            else:
                top_file = random.choice(normal_tops)
        else:
            top_file = ''

        if got_glasses:
            if random.random() < RARE_PROB:
                glasses_file = random.choice(rare_glasses)
            else:
                glasses_file = random.choice(normal_glasses)
        else:
            glasses_file = ''


        # check design existance
        design = []
        design.append(top_file)
        design.append(glasses_file)
        design_str = ",".join(design)+f",{body_type},{body_color}"
        if (design_str in existing_designs):
            continue
        else:
            existing_designs.append(design_str)
            print(f'generated {len(existing_designs)}/{rows*cols} unique designs', end="\r", flush=True)


        # render selected accessories
        if got_top:
            top_path = osp.join(TOP_DIR, top_file)
            accessory = Image.open(top_path)
            x, y = get_top_left_coord(render, accessory, OFFSET[body_type]["top"][0], OFFSET[body_type]["top"][1])
            render.paste(accessory, (x,y), accessory)
        if got_glasses:
            glasses_path = osp.join(GLASSES_DIR, glasses_file)
            accessory = Image.open(glasses_path)
            x, y = get_top_left_coord(render, accessory, OFFSET[body_type]["glasses"][0],  OFFSET[body_type]["glasses"][1])
            render.paste(accessory, (x,y), accessory)


        # cvt to cv2 and resize
        cv2_img = np.array(render)
        cv2_img = cv2_img[:, :, ::-1].copy()
        cv2_img = cv2.resize(cv2_img, unit_size)
        generated_imgs.append(cv2_img)


    # generate image grid
    img_tile = [generated_imgs[i*cols:(i+1)*cols] for i in range(rows)]
    res = render_tile(img_tile)

    # cv2.imshow('overlay', res)
    # cv2.waitKey(0)
    # # if cv2.waitKey(0) & 0xFF == ord('q'):
    # #     break
    #     #closing all open windows
    # cv2.destroyAllWindows()

    # write to file
    cv2.imwrite('../res/result.jpg', res)
