#coding=utf-8
import MySQLdb

li=[];
li_de=[];
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='weather',charset='utf8')
    cur=conn.cursor()
    cur.execute('select * from record order by date desc limit 16')
    results=cur.fetchall()
    for r in results:
        li.append('\"'+str(r[0])[8:10]+'日\"')
        li.append(str(r[1]))
        li.append(str(r[2]))
        li.append(str(r[3]))
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

l=len(li)
i=0
for j in range(0,l/4):
    li_de.append('\"date'+str(j)+'\":'+str(li[i]))
    i=i+1
    li_de.append('\"low'+str(j)+'\":'+str(li[i]))
    i=i+1
    li_de.append('\"high'+str(j)+'\":'+str(li[i]))
    i=i+1
    li_de.append('\"pm'+str(j)+'\":'+str(li[i]))
    i=i+1
ld=len(li_de)	
for k in range(0,ld):
    print li_de[k]

	
f=open(r'record.html','w')
f.write('[{')	

for i in range(0,ld-1):
	f.write(li_de[i]+',')
f.write(li_de[ld-1])
f.write('}]')
f.close()

print 'Update record success'
#raw_input()
