import sys
import cv2
import glob

size=(1800,1200)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter('video.mp4',fourcc, 20.0, size)

if not video.isOpened():
    print("can't be opened")
    sys.exit()

for i in range(1,180+1):
    print(i)
    pic_data=glob.glob("images_png/"+str(i)+".png")
    for j in range(len(pic_data)):
        img=pic_data[j]
        img=cv2.imread(img)#画像を読み込む
        img=cv2.resize(img,size)
        video.write(img)

                       

video.release()
print('written')