txt=open('hello.txt','r')
txt_read=txt.read()
txt.close()

jpg=open('hello.jpg','a+')
jpg.write(txt_read)
jpg.close()

jpg=open('hello.jpg','rb')
hello=jpg.read()
q=open('../hello2/hello.jpg','wb')
q.write(hello)
print('ok')
q.close()










