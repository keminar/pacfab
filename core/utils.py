# encoding: utf-8

import os
import importlib
from fabric.api import *
from module.common import *

class utils():
	def release(self):
		with quiet():
			output = run('head -n 1 /etc/issue|cut -d" " -f1')
			return output.lower()
	
	def module(self):
		os = self.release()
		if (os == 'debian' or os == 'ubuntu'):
			return 'module.debian'
		elif(os == 'redhat' or os == 'centos' or os == 'fedora'):
			return 'module.redhat'
		else:
			raise Exception("不支持的操作系统")

	def initClass(self, name):
		moduleName = self.module() + '.' + name
		modulePath = moduleName.replace(".", "/") + '.py'
		if not os.path.exists(modulePath):
			moduleName = 'module.common.' + name
		module = importlib.import_module(moduleName)
		instanceClass = getattr(module, name)
		initClass = instanceClass()
		return initClass
