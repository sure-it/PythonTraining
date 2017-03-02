from PIL import Image
import binascii
import zlib
a="789c9d940b0e80300843af04f1fe7733313196f6cd5fc874930e3ae8dc6afb673dac8e717acea7631475216abc13a3b12eafee6bc4f017cffbb44bd93b738fac5ee7cfe7ca1ae6f01adef7a41628cd32f934fa1a7666169d3943d247430caf8acf9517afbd7e8a59ad93a9abd63badb3b779e85c69a49d8ce7f57cab8954a2736436f3acb312d4ad44937ee8eeccbb9c78ba9515fe953af91fa11ee7c1fd48544734d73b292cb37cb21d0a2d1b33"
qq=binascii.a2b_hex(a)
ww=zlib.decompress(qq)
str2=binascii.a2b_hex(ww)
str=str2.decode('gbk')
#print(len(str))


MAX = 27
pic = Image.new("RGB",(MAX, MAX))
i=0
for y in range (0,MAX):
    for x in range (0,MAX):
        if(str[i] == '1'):
            pic.putpixel([x,y],(0, 0, 0))
        else:
            pic.putpixel([x,y],(255,255,255))
        i = i+1
pic.show()
pic.save("flag.png")

