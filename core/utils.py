# encoding: utf-8

import os
import importlib
from fabric.api import *
from module.common import *

class utils():

	# 系统
	def release(self):
		with quiet():
			return run('head -n 1 /etc/issue|cut -d" " -f1').lower()

	# 系统 32位64位
	def bit(self):
		with quiet():
			return run('getconf LONG_BIT')

	# 系统版本
	def version(self):
		with quiet():
			return run('head -n 1 /etc/issue|cut -d" " -f3|cut -d"." -f1')

	# 自定义模块
	def module(self):
		os = self.release()
		if (os == 'debian' or os == 'ubuntu'):
			return 'module.debian'
		elif(os == 'redhat' or os == 'centos' or os == 'fedora'):
			return 'module.redhat'
		else:
			raise Exception("不支持的操作系统")

	# 实例化模块
	def initClass(self, name):
		moduleName = self.module() + '.' + name
		modulePath = moduleName.replace(".", "/") + '.py'
		if not os.path.exists(modulePath):
			moduleName = 'module.common.' + name
		module = importlib.import_module(moduleName)
		instanceClass = getattr(module, name)
		initClass = instanceClass()
		return initClass

	# 增加用户
	def adduser(self, user, group = None):
		if (group is None):
			group = user
		with quiet():
			run('grep "^' + group + ':" /etc/group > /dev/null || groupadd ' + group)
			out = run('grep "^' + user + ':" /etc/passwd > /dev/null 2>&1;echo $?')
		if (out == "0"):
			run('usermod -g ' + group + ' ' + user)
		else:
			run('useradd -g ' + group + ' ' + user)

