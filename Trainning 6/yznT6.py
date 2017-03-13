import requests
import re

def get_mate(url):                              #对界面进行处理，获取图片地址
        r=requests.get(url)                     #访问目标地址
        qq=r.text                               #读取内容
        zz='https://imgsa.baidu.com/forum/w\S{50,90}jpg'        #设置正则条件
        a=re.findall(zz,qq)                                     #进行正则筛选图片
        return a



def save(img):                                                  #对图片进行保存操作
    for i in img:                                               #循环，分别对每个图片进行操作
        filename=i.split('/')[-1]                               #设置命名规则
        with open(filename,'wb') as f:                          #以二进制发送打开文件
            img=requests.get(i)                                 #访问并获取图片信息
            im=img.content                                      #读取图片内容
            f.write(im)                                         #把图片内容写入到文件中
            f.close()                                           #关闭文件
            print('ok')                                         
        
def main(url):                                                  #设置个总开关，分别管理
    q=get_mate(url)                                             
    save(q)
    
if __name__=='__main__':
    main("https://tieba.baidu.com/p/3682022093?pn=1")


























