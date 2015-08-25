# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class vim(base):

	def require(self):
		str = base.require(self)
		return str + ',git'

	def check(self):
		with quiet():
			output = run('test -e /root/.vimrc;echo $?')
			return output
	def lock(self):
		return '/root/.vimrc'

	def install(self):
		with cd(conf.BASE_DIR + '/dist/src/'):
			run('rm -rf vim')
			run('git clone ' + conf.VIM_URL)
			run('mkdir -p /root/.vim')
			run('cp -rf vim/.vim/* /root/.vim/')
			run('cp -f  vim/.vimrc /root/')
