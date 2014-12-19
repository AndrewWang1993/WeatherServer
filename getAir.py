#coding=utf-8
import urllib,re,MySQLdb,time,datetime

y=time.strftime("%Y")
m=time.strftime("%m")
d=time.strftime("%d")

now=y+'-'+m+'-'+d
pm='-1'
print now

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getRel(html,reg):
    mre = re.compile(reg)
    relList = re.findall(mre,html)
    return relList


html = getHtml("http://www.pm25.in/shenzhen")
reg1 = r'<div class.*="value">\s+([\d|.]+)\s+</div>'#air value
reg2 = r'<div class="level">\s+<h4>\s+(.+)\s+</h4>'   #index
reg3 = r'<p>建议采取的措施：\s+(.+)\s+</p>'           #excress suggest


val=getRel(html,reg1)
index=getRel(html,reg2)
suggest=getRel(html,reg3)

mlist=val+index+suggest
pm=str(mlist[1])
print mlist

_mlist = ['aqi','pm2_5_24h','PM10/1h','CO/1h','NO2/1h','O3/1h','O3/8h','SO2/1h','quality','suggest']
print _mlist

f=open(r'AirCondition.html','w')
f.write('[{')

len=len(mlist)
for i in range(0,len-2):
    f.write('\"'+_mlist[i]+'\":'+mlist[i]+',')
    
f.write('\"'+_mlist[len-2]+'\":\"'+mlist[len-2]+'\",')
f.write('\"'+_mlist[len-1]+'\":\"'+mlist[len-1]+'\"')
f.write('}]')
f.close()

print now,pm	
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='weather',charset='utf8')
    cur=conn.cursor()
    sql = "UPDATE record SET pm2_5 = %s WHERE date = '%s'" % (str(pm),str(now))
    print sql
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])


print 'Air update and inser Database Success'
#raw_input()
