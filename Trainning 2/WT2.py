import os
f=open("D:\\Desktop\\copy\\hello1\\hello.jpg","r+b")
f_read=f.readlines()
#print f_read
f1=open("D:\\Desktop\\copy\\hello1\\hello.txt","r")
f1_read=f1.read()
#print f1_read
f.write(f1_read)
f.close
f1.close
os.system("copy D:\\Desktop\\copy\\hello1\\hello.jpg D:\\Desktop\\copy\\hello2\\hello.jpg")

