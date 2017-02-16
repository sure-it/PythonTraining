import os
import os.path

path = "f:" + os.sep + "depolice"

# def tree(level,path):
#     for i in os.listdir(path):
#         print('|  '*(level + 1) + i)
#         if os.path.isdir(path+i):
#             tree(level+1, path+i)

# tree(0, path+os.sep) 


# for x in os.walk(path):
# 	print x[0]
# 	print x[1]
# 	print x[2]
# 	print '*' * 20

# for i in  os.system('tree /f f:/'):


# for filename in os.listdir(path):
# 	print filename







def processDirectory ( args, dirname, filenames ):
	print 'Directory',dirname
	for filename in filenames:
		print ' File',filename
		os.path.walk(path, processDirectory, None )