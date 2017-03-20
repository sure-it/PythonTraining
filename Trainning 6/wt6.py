import re
import urllib


url="https://tieba.baidu.com/p/3682022093?pn=1"
def geturl(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
    
    
def getimg(html):
    reg=re.compile('https://img.*?.jpg')
    url=re.findall(reg,html)
#    print url
    x=0
    for i in url:
        print i
        urllib.urlretrieve(i,"D:\\Desktop\\%s.jpg" % x)
        x=x+1
        
    

q=geturl(url)
getimg(q)
