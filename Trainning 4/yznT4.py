import os
import os.path
def qwer(qw):          #返回文件的绝对路径
    qq=[]
    #print(qw)
    file=os.listdir(qw)         #获取目录下的文件名
    #print(file)
    os.chdir(qw)                #切换到要查询的目录
    a=os.getcwd()               #列出当前的绝对路径
    for q in file:
        ww=os.path.join(a,q)    #融合成绝对路径
        qq.append(ww)
    return qq
    


    
def asdf(er):                   #判断是不是目录
    mulu=[]
    mulu2=qwer(er)
    for q in mulu2:
        if os.path.isdir(q):
            asdf(q)
            mulu.append(q)
        else:
            print(q)
    return mulu

if __name__=='__main__':
    list=input(r"输入要检查的目录:")
    asdf(list)



