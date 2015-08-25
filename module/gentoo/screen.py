# encoding: utf-8

import conf
from fabric.api import *
from module.common.screen import screen
class screen(screen):
	def install(self):
		run('emerge -n app-misc/screen')
		super(screen, self).install()
