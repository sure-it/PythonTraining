f=open('D:\\Desktop\\randlist.txt')
s=f.read()      #读取文件
global list_all
global list_to_statistic
def tran_s_to_list(s):
        list_all=[]
        z={}
        l=len(s)        #得到长度，遍历
        for x in xrange(0,l):
                if not s[x] in list_all:
                        list_all.append(s[x])#当x不在list中，即第一次出现，追加到list_all中
                #print list_all
        for x in list_all:
            list_count=s.count(x)#统计字符出现的次数
            #print(x)
            #print list_count
            z.update({x:list_count})
        #print z
        sorted_z = sorted(z.iteritems(), key=lambda x : x[1])#排序输出
        print sorted_z
        #print "Value : %s" % sorted_z.values()

tran_s_to_list(s)

