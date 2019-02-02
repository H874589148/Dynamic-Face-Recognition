# 1.导入库
#import cv2

# 2.加载人脸模型
#img = cv2.imread('F:\github_repository\Dynamic-Face-Recognition\image1.jpg')

# 3.创建窗口
#cv2.namedWindow('Hawkeye 窗口')

# 4.显示图片
#cv2.imshow('Hawkeyetest',img)

# 5.暂停窗口
#cv2.waitKey(0)

# 6.关闭窗口
#cv2.destoryAllWindows()

#1.导入库
#import cv2
# 2.加载图片
#img = cv2.imread('F:\github_repository\Dynamic-Face-Recognition\image1.jpg')
# 3.加载人脸模型
#face = cv2.CascadeClassifier("F:\github_repository\Dynamic-Face-Recognition\image1.jpg")
# 4.调整图片灰度(人脸识别不用彩色消耗性能，灰度可以提高性能)
#gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# 5.检查人脸
#faces = face.detectMultiScale(gray)
# 6.标记人脸
#for (x,y,w,h) in faces:
    #里面有四个参数 1.写图片 2.坐标原点 3.识别大小 4.颜色 5.线宽
    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),10)
# 7.创建窗口
#cv2.namedWindow('Hawkeye 窗口')
# 8.显示图片
#cv2.imshow('Hawkeyetest',img)
# 9.暂停窗口
#cv2.waitKey(0)
# 10.关闭窗口
#cv2.destoryAllWindows()

#打开摄像头
#capture = cv2.VideoCapture(0)
#获取摄像头实时画面
#while True
    #读取摄像头帧画面
    #ret,frame = capture.read()
    #显示图片 渲染画面
    #cv2.imshow('Hawkeye',frame)
    #暂停窗口
    #if cv2.waitKey(5) & 0xFF == ord('q'):
        #break

#释放资源
#capture.release()