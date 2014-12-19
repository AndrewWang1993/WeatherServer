#coding=utf-8

import urllib,re,MySQLdb,ConfigParser,datetime,time

y=time.strftime("%Y")
m=time.strftime("%m")
d=time.strftime("%d")

now=y+'-'+m+'-'+d
todaylow=99;
todayhigh=99;

print now

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getRel(html,reg):
    mre = re.compile(reg)
    relList = re.findall(mre,html)
    return relList

html = getHtml("http://tianqi.2345.com/shenzhen/59493.htm")
html1 = getHtml("http://weather.com.cn/weather/101280601.shtml")
reg1 = r'<font class="[a-z]{3,4}">(-?\w+).{0,2}</font>'  #temputer   
reg2 = r'</span>\s+</em>\s+<i>(.+)</i>'     #wind
reg3 = r'<p class="wea">(.+)</p>\s+<p class="tem tem\d">'     #index   
reg4 = r'<section class="mask ct">\s.+\s.+\s.+7d1"><b>(.+)</b>'        #feeling
reg5 = r'<section class="mask ct">\s.+\s.+\s.+7d1"><b>.+</b>(.+)</aside>' #wearing suggest

temputer=getRel(html,reg1)
wind=getRel(html1,reg2)
index=getRel(html1,reg3)
feeling=getRel(html1,reg4)
suggest=getRel(html1,reg5)
todayhigh=temputer[1]
todaylow=temputer[0]

i=1
while i<len(temputer):
    temputer[i-1]=temputer[i]+"℃~"+temputer[i-1]+"℃"
    del temputer[i]
    i=i+1
temputer=temputer[0:7]


mlist=temputer+index+wind+feeling+suggest

print mlist

_mlist = ['temp1','temp2','temp3','temp4','temp5','temp6','temp7','weather1','weather2','weather3','weather4','weather5','weather6','weather7','wind1','wind2','wind3','wind4','wind5','wind6','wind7','index','index48_d']

f=open(r'Weather.html','w')

f.write('{\"weatherinfo\":{\"city\":\"深圳\",\"city_en\":\"shenzhen\",\"date_y\":\"'+y+'年'+m+'月'+d+'日\",\"week\":\"星期五\",')
	   
	   
j=len(_mlist)
k=len(mlist)
print j,k

for i in range(0,j-1):
    f.write('\"'+_mlist[i]+'":"'+mlist[i]+'",')
	
	
f.write('\"'+_mlist[j-1]+'":"'+mlist[j-1]+'"'+'}}')


f.close()



try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='weather',charset='utf8')
    cur=conn.cursor()
    val=[now,todaylow,todayhigh,'-1']
    print val
    cur.execute('insert into record values(%s,%s,%s,%s)',val)
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

	
print 'Update and inser Database Success'
#raw_input()

