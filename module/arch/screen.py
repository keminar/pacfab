# encoding: utf-8

import conf
from fabric.api import *
from module.common.screen import screen
class screen(screen):
	def install(self):
		run('pacman -S screen --noconfirm --need')
		super(screen, self).install()
