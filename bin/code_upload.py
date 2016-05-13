#/usr/bin/env python
# -*- coding: utf-8 -*-




import time
from optparse import OptionParser
from fabric.api import *
import ConfigParser
import logging


#定义参数格式

#usage = "usage: %prog [options] arg1 agr2"
#parser = OptionParser(usage=usage)
#(options, args) = parser.parse_args()






#配置文件
conf = ConfigParser.ConfigParser()
conf.read('../conf/upload.conf')
sections = conf.sections()
env.passwords = {}
env.hosts = []
env.roledefs = {}


for host_info in sections:
    host = conf.get(host_info,'host')
    port = conf.get(host_info,'port')
    user = conf.get(host_info,'user')
    password = conf.get(host_info,'password')
    role = conf.get(host_info,'role')

    env.hosts.append('%s@%s:%s'%(user,host,port))
    env.passwords['%s@%s:%s'%(user,host,port)] = password

    if env.roledefs.has_key(role):
        env.roledefs[role].append(host)
    else:
        env.roledefs[role] = []
        env.roledefs[role].append('%s@%s:%s'%(user,host,port))




print env.roledefs

#定义日志








a='webserver'
@roles('%s' %a)
def web():
    run('ls -l')






execute(web)
