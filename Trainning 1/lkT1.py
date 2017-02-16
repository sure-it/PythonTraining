file_object = open('randlist.txt','r')  #打开文件，只读
all_the_txt = file_object.read()        #读取文件
all_the_txt_set = set(all_the_txt)      #消除重复元素
txt_total = {}                          #创建字典
for i in all_the_txt_set:               #循环查找字符
    total = all_the_txt.count(i)        #统计字符数量
    txt_total.update({i:total})         #写入字典
lk = sorted(txt_total.items(),key=lambda l:l[-1])  
for o in lk:
    print(o,end='\n')

 

