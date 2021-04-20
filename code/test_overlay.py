# -*- coding: utf-8 -*-
# @Author: fyr91
# @Date:   2021-04-20 10:38:55
# @Last Modified by:   fyr91
# @Last Modified time: 2021-04-20 10:49:52
from PIL import Image

base = Image.new('RGB', (600, 600), (155, 93, 229))
body = Image.open("../assets/base/pd_01/black.png")
accessory = Image.open("../assets/hat/1.png")

base.paste(body, (0 , 0), body)
base.paste(accessory, (0 , 80), accessory)
base.show()
