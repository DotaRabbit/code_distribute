#/usr/bin/env python
# -*- coding: utf-8 -*-





from optparse import OptionParser
from fabric.api import local,lcd,run,env,hosts,execute,roles,put
import ConfigParser
import logging


#定义参数格式

usage = "usage: %prog [options] arg1 agr2"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()





#配置文件
conf = ConfigParser.ConfigParser()
conf.read('../conf/upload.conf')
sections = conf.sections()
print sections
ip = conf.get('host1','ip')
print ip


#定义日志









