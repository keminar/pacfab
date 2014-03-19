# encoding: utf-8

import conf
from fabric.api import *
from module.common.base import base
class vim(base):

	def require(self):
		str = base.require(self)
		return str + ',git'

	def check(self):
		with quiet():
			output = run('test -e /root/.vimrc;echo $?')
			return output

	def install(self):
		with cd(conf.BASE_DIR + '/dist/src/'):
			run('git clone git@github.com:keminar/vim.git')
			run('mkdir /root/.vim')
			run('cp -rf vim/.vim/* /root/.vim/')
			run('cp -f  vim/.vimrc /root/')
