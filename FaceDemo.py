# 1.导入库
import cv2

# 2.加载人脸模型
img = cv2.imread('F:\github_repository\Dynamic-Face-Recognition\image1.jpg')

# 3.创建窗口
cv2.namedWindow('Hawkeye 窗口')

# 4.显示图片
cv2.imshow('Hawkeyetest',img)

# 5.暂停窗口
cv2.waitKey(0)

# 6.关闭窗口
cv2.destoryAllWindows()