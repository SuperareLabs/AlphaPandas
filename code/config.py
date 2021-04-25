# -*- coding: utf-8 -*-
# @Author: fyr91
# @Date:   2021-04-20 10:27:18
# @Last Modified by:   fyr91
# @Last Modified time: 2021-04-25 19:21:07

# Directory config
BASE_DIR = '../assets/base/'  # dir for base
TOP_DIR = '../assets/top/'  # dir for hat
HAIR_DIR = '../assets/hair/'  # dir for hair
GLASSES_DIR = '../assets/glasses/'  # dir for glasses
HAND_DIR = "../assets/hands/"

# Probabililty
TOP_PROB = 0.5
HAIR_PROB = 0
GLASSES_PROB = 0.2
LEFT_HAND_PROB = 0.6
RIGHT_HAND_PROB = 0.6
RARE_PROB = 0.04

# BG color palette
BG_COLORS = [(155, 93, 229), (241, 91, 181), (0, 187, 249), (0, 245, 212)]
RARE_BG = (254, 228, 64)
BODY_TYPES = ['pd_01', 'pd_02', 'pd_03', 'pd_04']
# BG_COLOR = [(255,255,255)]
# BG_COLOR = [(237, 220, 210), (255, 241, 230), (253, 226, 228), (250, 210, 225), (197, 222, 221),
#             (219, 231, 228), (240, 239, 235), (214, 226, 233), (188, 212, 230), (153, 193, 222)]

OFFSET = {
    "pd_01": {
        "hair": [-4, 176],
        "glasses": [-4, 224],
        "top": [-4, 80],
        "right_hand": [-92, 320],
        "left_hand": [84, 320]
    },
    "pd_02": {
        "hair": [-4, 138],
        "glasses": [-4, 192],
        "top": [-4, 32],
        "right_hand": [-172, 288],
        "left_hand": [164, 288]
    },
    "pd_03": {
        "hair": [-4, 272],
        "glasses": [-4, 320],
        "top": [-4, 176],
        "right_hand": [-30, 368],
        "left_hand": [20, 368]
    },
    "pd_04": {
        "hair": [-4, 82],
        "glasses": [-4, 144],
        "top": [-4, 0],
        "right_hand": [-92, 256],
        "left_hand": [84, 256]
    },

}
