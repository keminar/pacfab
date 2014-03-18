# encoding: utf-8

import conf
from fabric.api import *
from module.common.init import init
class init(init):
	def install(self):
		run('yum update')
		run('yum install groupinstall "Development tools"')
