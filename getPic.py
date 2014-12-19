#coding=utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+\.jpg)" alt=\"\" style=\"display:none'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 2
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
    return imglist      
   
html = getHtml("http://news.163.com/photoview/00AP0001/78850.html#p=ACHF2ARC00AP0001")
print getImg(html)
