# encoding: utf-8

import conf
from fabric.api import *
from module.common.vim import vim
class vim(vim):
	def install(self):
		run('pacman -S vim --noconfirm --need')
		super(vim, self).install()
