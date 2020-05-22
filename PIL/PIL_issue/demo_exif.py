import numpy as np
import cv2

import PIL
from PIL import Image

s = '/Users/zhangxin/data_md/sunpp/2020-05-21-idcard73/good/214.jpg'
img_pil = Image.open(s)
print('PIL Image.open : ', img_pil.size, img_pil.mode)

img_cv = cv2.imread(s)
print('cv2.imread : ', img_cv.shape)
