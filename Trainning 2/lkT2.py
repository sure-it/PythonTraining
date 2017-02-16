path1 = 'copy/hello1/'
path2 = 'copy/hello2/'
import shutil
shutil.copyfile(path1+'hello.jpg',path2+'hello.jpg') #复制图像
##################################
f1 = open(path2+'hello.jpg','a+')
##################################
f2 = open(path1+'hello.txt',)
f2_msg = f2.read()
##################################
f1.write(f2_msg)
f1.close()
print('Done')






#读取和显示图像
#import cv2
#def showimg(imagePath):  
#    img = cv2.imread(imagePath)  #读取本地图片，目前OpevCV支持bmp、jpg、png、tiff  
#    cv2.namedWindow("Image")     #创建一个窗口用来显示图片  
#    cv2.imshow("Image", img)     #显示图片  
#    cv2.waitKey (0)              #等待输入,这里主要让图片持续显示。  
#    cv2.destroyAllWindows()      #释放窗口  
  
#if __name__ == '__main__':   
#    imagePath = path1+'hello.jpg'
#    showimg(imagePath)   
