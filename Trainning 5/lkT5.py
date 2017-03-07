from PIL import Image
import binascii
import zlib
data_1="789c9d940b0e80300843af04f1fe7733313196f6cd5fc874930e3ae8dc6afb673dac8e717acea7631475216abc13a3b12eafee6bc4f017cffbb44bd93b738fac5ee7cfe7ca1ae6f01adef7a41628cd32f934fa1a7666169d3943d247430caf8acf9517afbd7e8a59ad93a9abd63badb3b779e85c69a49d8ce7f57cab8954a2736436f3acb312d4ad44937ee8eeccbb9c78ba9515fe953af91fa11ee7c1fd48544734d73b292cb37cb21d0a2d1b33"
data_2=binascii.a2b_hex(data_1)         #十六进制转换为二进制
data_3=zlib.decompress(data_2)          #二进制zlib解压缩
str2=binascii.a2b_hex(data_3)           #解压缩之后的数据再转换为二进制
str=str2.decode('gbk')                  #字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，
                                        #即先将其他编码的字符串解码（decode）成unicode，将gbk编码转换成unicode类型。
MAX_num = len(str)                      #统计数据数目
MAX=int(MAX_num ** 0.5)                 #对数据数目开平方根，因为二维码是正方形。
pic = Image.new("RGB",(MAX, MAX))       #新建一张图片
i=0
for y in range (0,MAX):
    for x in range (0,MAX):
        if(str[i] == '1'):
            pic.putpixel([x,y],(0, 0, 0))       #putpixel将坐标为(x,y)的像素点变为(0,0,0)
        else:
            pic.putpixel([x,y],(255,255,255))   #putpixel将坐标为(x,y)的像素点变为(255,255,255)
        i = i+1
pic.show()
#pic.save("flag.png")
