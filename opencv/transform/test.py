
import math
import numpy as np
import cv2


img_path = '../232.jpg'
rotate_angle = 30
theta = math.radians(rotate_angle)
print(rotate_angle, theta)

img = cv2.imread(img_path)
print(img_path, img.shape)

h, w = img.shape[:2]

# 以中心为原心为旋转
half_w = int(w // 2 + 1)
half_h = int(h // 2 + 1)
# 对右下顶点进行旋转，最大的宽度和高度
new_w1 = (math.cos(theta) * half_w - math.sin(theta) * half_h) * 2
new_h1 = (math.sin(theta) * half_w + math.cos(theta) * half_h) * 2
print("image shape : {}, (new_w, new_h) : {},{}".format(img.shape, new_w1, new_h1))

# 对右上顶点进行旋转，最大的宽度和高度
new_w2 = (math.cos(theta) * half_w - math.sin(theta) * -half_h) * 2
new_h2 = (math.sin(theta) * half_w + math.cos(theta) * -half_h) * 2
print("image shape : {}, (new_w, new_h) : {},{}".format(img.shape, new_w2, new_h2))

# 求出最大的宽度和高度
new_w = int(max(abs(new_w1), abs(new_w2), w))
new_h = int(max(abs(new_h1), abs(new_h2), h))
print(new_w, new_h)

M = cv2.getRotationMatrix2D((w//2, h//2), rotate_angle, 1.0)
M[0, 2] += (new_w - w) // 2
M[1, 2] += (new_h - h) // 2
print(M)


img_res = cv2.warpAffine(img, M, (new_w, new_h))
cv2.imwrite("res.jpg", img_res)
