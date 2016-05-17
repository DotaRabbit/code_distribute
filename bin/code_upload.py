#/usr/bin/env python
# -*- coding: utf-8 -*-




import time
from optparse import OptionParser
from fabric.api import *
import ConfigParser
import logging
from progressbar import *
import os
import threading


#定义参数格式

#usage = "usage: %prog [options] arg1 agr2"
#parser = OptionParser(usage=usage)
#(options, args) = parser.parse_args()






#配置文件信息
host_conf = ConfigParser.ConfigParser()
host_conf.read('../conf/host.conf')
host_sections = host_conf.sections()

deploy_conf = ConfigParser.ConfigParser()
deploy_conf.read('../conf/deploy.conf')
deploy_sections = deploy_conf.sections()

env.passwords = {}
env.hosts = []
env.roledefs = {}


for host_info in host_sections:
    host = host_conf.get(host_info,'host')
    port = host_conf.get(host_info,'port')
    user = host_conf.get(host_info,'user')
    password = host_conf.get(host_info,'password')
    role = host_conf.get(host_info,'role')

    env.hosts.append('%s@%s:%s'%(user,host,port))
    env.passwords['%s@%s:%s'%(user,host,port)] = password

    if env.roledefs.has_key(role):
        env.roledefs[role].append('%s@%s:%s' % (user, host, port))
    else:
        env.roledefs[role] = []
        env.roledefs[role].append('%s@%s:%s' % (user, host, port))






#定义日志




file_size = os.path.getsize('C:\puhui-uc-server-restful.zip')

print file_size
def puttask():
    with settings(hide('everything')):
        put('C:\puhui-uc-server-restful.zip','/home/xuning/a.zip')

def get_size():
    with settings(hide('everything')):
        return run("ls -l /home/xuning/a.zip|awk '{print $5}'")


def loading():

    widgets = [Bar('#'), ' ', 'Uploading:', Percentage(), ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=file_size)
    pbar.start()
    size = 0
    while size <= file_size:
            size = get_size()
            pbar.update(size)
            time.sleep(0.5)
    pbar.finish()
def execute_puttask():
    execute(puttask)
def execute_loading():
    execute(loading)
t1 = threading.Thread(target= execute_puttask)
t2 = threading.Thread(target= execute_loading)
t1.start()
t2.start()