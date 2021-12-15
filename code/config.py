# -*- coding: utf-8 -*-
# @Author: fyr91
# @Date:   2021-04-20 10:27:18
# @Last Modified by:   yirui
# @Last Modified time: 2021-12-15 17:41:01

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
RARE_PROB = 0.25

# BG color palette
BG_COLORS = [(155, 93, 229), (241, 91, 181), (0, 187, 249), (0, 245, 212)]
RARE_BG = (254, 228, 64)
# BG_FILES = ["blue_blue.jpg", "green_green.jpg", "pink_orange.jpg", "purple_blue.jpg"]
# RARE_BG_FILE = "yellow_red.jpg"
BG_FILES = ["glass_blue.jpg", "glass_green.jpg", "glass_purple.jpg", "glass_pink.jpg"]
RARE_BG_FILES = ["pink_orange.jpg", "rare1.jpg", "rare2.jpg"]
BODY_TYPES = ['pd_01', 'pd_02', 'pd_03', 'pd_04']
# BG_COLOR = [(255,255,255)]
# BG_COLOR = [(237, 220, 210), (255, 241, 230), (253, 226, 228), (250, 210, 225), (197, 222, 221),
#             (219, 231, 228), (240, 239, 235), (214, 226, 233), (188, 212, 230), (153, 193, 222)]

OFFSET = {
    # normal
    "pd_01": {
        # "hair": [0, 176],
        "glasses": [0, 224],
        "top": [0, 80],
        "right_hand": [-88, 320],
        "left_hand": [88, 320]
    },
    # fat
    "pd_02": {
        # "hair": [0, 138],
        "glasses": [0, 192],
        "top": [0, 32],
        "right_hand": [-168, 288],
        "left_hand": [168, 288]
    },
    # tiny
    "pd_03": {
        # "hair": [0, 272],
        "glasses": [0, 320],
        "top": [0, 176],
        "right_hand": [-24, 368],
        "left_hand": [24, 368]
    },
    # tall
    "pd_04": {
        # "hair": [0, 82],
        "glasses": [0, 144],
        "top": [0, 0],
        "right_hand": [-88, 256],
        "left_hand": [88, 256]
    },

}
