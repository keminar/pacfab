# encoding: utf-8

import conf
from fabric.api import *
from module.common.base import base
class anmp(base):
	def install(self):
		pass

	def require(self):
		return 'apache,nginx,mysql,php'
