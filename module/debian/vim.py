# encoding: utf-8

import conf
from fabric.api import *
from module.common.vim import vim
class vim(vim):
	def install(self):
		run('apt-get install -y vim')
		super(vim, self).install()
