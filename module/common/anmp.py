# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class anmp(base):
	def install(self):
		pass

	def check(self):
		return "1"

	def require(self):
		return 'apache,nginx,mysql,php'
