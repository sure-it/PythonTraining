import os
import shutil

command = "copy hello.jpg/b + hello.txt/a test.jpg"  #定义cmd的命令
os.system(command)       #调用shell脚本
shutil.move("test.jpg","../hello2/test.jpg")  #移动到指定文件夹  
