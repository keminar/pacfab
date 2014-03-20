# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class init(base):
	def prepare(self):
		run('mkdir -p ' + conf.INSTALL_DIR + '/{bin,opt,srv}')
		run('mkdir -p ' + conf.BASE_DIR + '/dist/src')

	def install(self):
		run('touch /var/log/install.log')

	def require(self):
		return ''

	def check(self):
		with quiet():
			output = run('test -e /var/log/install.log;echo $?')
			return output
