import os
import os.path

def file_1(b):                      #定义文件检查函数
    file_list=[]
    file_name=os.listdir(b)         #获取当前路径下的文件名称
    os.chdir(b)                     #切换到指定目录，为下一步获取当前路径做准备
    new_path2=os.getcwd()           #获取当前路径
    for i in file_name:
        merge_path_and_file=os.path.join(new_path2,i)       #合并路径和文件名称添加到表里
        file_list.append(merge_path_and_file)       
    return file_list

def input_path(a):                  #定义目录检查函数
    path=[]
    path2=file_1(a)                 #调用文件检查函数
    for o in path2:
        if os.path.isdir(o):        #判断是否为目录：
            input_path(o)           #   是：调用文件检查函数
            path.append(o)
        else:
            print(o)                #   否：打印文件检查函数合并的绝对路径
    return path


if __name__=='__main__':            #输入需要查看的目录【绝对或者相对路径】
    list=input(r"输入要检查的目录:")
    input_path(list)



#本题目答案参考了yuzhengnan的答案，研究了好半天终于想明白了，^_^



