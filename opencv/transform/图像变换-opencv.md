


对于平面区域：
1. 使用2 * 3 矩阵的变换，称为**仿射变换**。
2. 使用3 * 3 矩阵的变换，称为**透视变换**。

# 1 仿射变换
## 1.1 密集仿射变换函数     cv::warpAffine

## 1.2 计算仿射映射矩阵     cv::getAffineTransform

## 1.3 计算映射矩阵         cv::getRotationMatrix2d
```python
import math
# 角度转为弧度
math.radians(30)
# 弧度转为角度
math.degrees(1.72)
```

## 1.4 计算稀疏仿射变换     cv::transform

## 1.5 逆仿射变换           cv::invertAffineTransform

# 2 透视变换
## 2.1 密集透视变换         cv::warpPerpective()

## 2.2 计算透视映射矩阵      cv::getPerspectiveTransform()

## 2.3 稀疏透视变换         cv::perspectiveTransform()





