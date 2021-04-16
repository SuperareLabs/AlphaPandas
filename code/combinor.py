# -*- coding: utf-8 -*-
# @Author: User
# @Date:   2021-04-16 11:05:13
# @Last Modified by:   fyr91
# @Last Modified time: 2021-04-16 18:45:21
import cv2
import os
from os import path as osp
import numpy as np
import random
import itertools
import time

BASE_DIR = '../assets/base/'
HAT_DIR = '../assets/hat/'
HAIR_DIR = '../assets/hair/'
GLASSES_DIR = '../assets/glasses/'

def show_assets_dim(base):
    for file in os.listdir(base):
        img = cv2.imread(osp.join(base, file))
        print(img.shape)

def overlay_transparent(base, accessory, x, y):
    """
    @brief      Overlays a transparant PNG onto another image using CV2

    @param      base    The background image
    @param      accessory  The transparent image to overlay (has alpha channel)
    @param      x                 x location to place the top-left corner of our overlay
    @param      y                 y location to place the top-left corner of our overlay

    @return     Background image with overlay on top
    """

    bg_img = base.copy()

    # Extract the alpha mask of the RGBA image, convert to RGB
    b,g,r,a = cv2.split(accessory)
    overlay_color = cv2.merge((b,g,r))

    # Apply some simple filtering to remove edge noise
    mask = cv2.medianBlur(a,5)

    h, w, _ = overlay_color.shape
    roi = bg_img[y:y+h, x:x+w]

    # Black-out the area behind the logo in our original ROI
    img1_bg = cv2.bitwise_and(roi.copy(),roi.copy(),mask = cv2.bitwise_not(mask))

    # Mask out the logo from the logo image.
    img2_fg = cv2.bitwise_and(overlay_color,overlay_color,mask = mask)

    # Update the original image with our new ROI
    bg_img[y:y+h, x:x+w] = cv2.add(img1_bg, img2_fg)

    return bg_img

def get_top_left_coord(base, img,  offset_x = -4, offset_y = 0):
    h1,w1,_ = base.shape
    h2,w2,_ = img.shape

    x = (w1-w2)/2 + offset_x
    y = 240 + offset_y

    return int(x), int(y)


def render_tile(img_list):
    return cv2.vconcat([cv2.hconcat(img_list_h) for img_list_h in img_list])

offset_dict = {
    "pd_01": {
        "hair": [-4, -100],
        "glasses": [-4, -10],
        "hat": [-4, -130],
    },
    "pd_02": {
        "hair": [-4, -150],
        "glasses": [-4, -40],
        "hat": [-4, -170],
    },
    "pd_03": {
        "hair": [12, 0],
        "glasses": [12, 86],
        "hat": [12, -26],
    },
    "pd_04": {
        "hair": [12, -190],
        "glasses": [12, -90],
        "hat": [12, -210],
    },

}

BG_COLOR = [(155, 93, 229), (241, 91, 181), (254, 228, 64), (0, 187, 249), (0, 245, 212)]

# BG_COLOR = [(237, 220, 210), (255, 241, 230), (253, 226, 228), (250, 210, 225), (197, 222, 221),
#             (219, 231, 228), (240, 239, 235), (214, 226, 233), (188, 212, 230), (153, 193, 222)]


if __name__ == '__main__':
    # show_assets_dim(GLASSES_DIR)
    existing_designs = []

    hairs = os.listdir(HAIR_DIR)
    hats = os.listdir(HAT_DIR)
    glasses = os.listdir(GLASSES_DIR)

    rows = 14
    cols = 14
    unit_size = (200,200)
    generated_imgs = []

    while len(generated_imgs) < rows*cols:

        base = np.zeros((600,600,3), np.uint8)
        base[:]=random.choice(BG_COLOR)
        base = cv2.cvtColor(base, cv2.COLOR_RGB2BGR)

        base_name = random.choice(['pd_01','pd_02','pd_03','pd_04'])
        body = cv2.imread(f'../assets/base/{base_name}_trans.png', -1)

        base = overlay_transparent(base, body, 0, 0)

        design = []

        # determine accessories
        got_hair = random.random()>0.5
        got_hat = random.random()>0.5
        got_glasses = random.random()>0.5

        if got_hair:
            hair_file = random.choice(hairs)
        else:
            hair_file = ''

        if got_hat:
            hat_file = random.choice(hats)
        else:
            hat_file = ''

        if got_glasses:
            glasses_file = random.choice(glasses)
        else:
            glasses_file = ''

        design.append(hair_file)
        design.append(hat_file)
        design.append(glasses_file)

        # check design existance
        design_str = ",".join(design)+f"-{base_name}"
        if (design_str in existing_designs) or design_str == ',,':
            # print('existed - pass')
            continue
        else:
            print(design_str)
            existing_designs.append(design_str)

        if got_hair:
            hair_path = osp.join(HAIR_DIR, hair_file)
            accessory = cv2.imread(hair_path, -1)
            x, y = get_top_left_coord(base, accessory, offset_dict[base_name]["hair"][0], offset_dict[base_name]["hair"][1])
            base = overlay_transparent(base, accessory, x, y)

        if got_hat:
            hat_path = osp.join(HAT_DIR, hat_file)
            accessory = cv2.imread(hat_path, -1)
            x, y = get_top_left_coord(base, accessory, offset_dict[base_name]["hat"][0], offset_dict[base_name]["hat"][1])
            base = overlay_transparent(base, accessory, x, y)

        if got_glasses:
            glasses_path = osp.join(GLASSES_DIR, glasses_file)
            accessory = cv2.imread(glasses_path, -1)
            x, y = get_top_left_coord(base, accessory, offset_dict[base_name]["glasses"][0],  offset_dict[base_name]["glasses"][1])
            base = overlay_transparent(base, accessory, x, y)

        base = cv2.resize(base, unit_size)
        generated_imgs.append(base)

    img_tile = [generated_imgs[i*cols:(i+1)*cols] for i in range(rows)]
    res = render_tile(img_tile)

    cv2.imshow('overlay', res)
    cv2.waitKey(0)
    # if cv2.waitKey(0) & 0xFF == ord('q'):
    #     break
        #closing all open windows
    cv2.destroyAllWindows()

    cv2.imwrite('../res/result.jpg', res)
