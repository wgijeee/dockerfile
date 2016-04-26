!/usr/bin/env python
#coding=utf-8
#wgijeee@qq.com
#访问特定URL。让PHP执行对应的任务

import urllib2
import time
import re
import datetime
#引入python模块

makeurl='http://localhost'
make=urllib2.urlopen(makeurl)
#联盟商家对账单

time.sleep(10)
#延时执行下一个

yunbiurl='http://localhost'
yunbi=urllib2.urlopen(yunbiurl)
#云币分配状态

now = datetime.datetime.now()
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
#获取当时间
tomake=make.read()
toyunbi=yunbi.read()
#抓取当前输出状态。

n='\n'
#换行符
file=open('/home/httpd/yunmakelog.log','a+')
yunbilog=n+otherStyleTime+n+tomake+n+n+otherStyleTime+n+toyunbi+n+n
file=file.write(yunbilog)
#追加日志
