# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class screen(base):

	def require(self):
		return ''

	def check(self):
		with quiet():
			output = run('test -e /root/.screenrc;echo $?')
			return output
	def lock(self):
		return '/root/.screenrc'

	def install(self):
		put(conf.BASE_DIR + '/conf/screen/screenrc', '/root/.screenrc')
