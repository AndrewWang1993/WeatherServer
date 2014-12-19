from threading import Timer
import datetime,time,os,urllib,re,MySQLdb

def delayrun1():

    execfile('getWeather.py')
    print 'getWeather.py'
    print '-'*30

def delayrun2():

    execfile('getSimpleWeather.py')
    print 'getSimpleWeather.py'
    print '-'*30

def delayrun3():

    execfile('getAir.py')
    print 'getAir.py'
    print '-'*30

def delayrun4():

    execfile('getRecord.py')
    print 'getRecord.py'
    print '-'*30


while True:
    delayrun1()
    time.sleep(15)
    delayrun2()
    time.sleep(15)
    delayrun3()
    time.sleep(10)
    delayrun4()
    time.sleep(1)
    print '*'*60
    time.sleep(1800)

