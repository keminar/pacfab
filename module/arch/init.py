# encoding: utf-8

import conf
from fabric.api import *
from core.utils import utils
from module.common.init import init
class init(init):
	def install(self):
		super(init, self).prepare()
		with quiet():
			if (run('grep "/etc/profile.d" /etc/profile') == ""):
				put(conf.BASE_DIR + '/conf/init/profile.tpl', conf.BASE_DIR)
				run('cat ' + conf.BASE_DIR + '/profile.tpl >> /etc/profile')
		run('pacman -S --noconfirm --need base-devel')
		run('pacman -S --noconfirm --need wget')
		run('pacman -S --noconfirm --need libjpeg-turbo libpng libxpm freetype2 libxslt libsasl')
		run('pacman -S --noconfirm --need curl libldap pcre')
		self.bit = utils().bit()
		if (self.bit == "32"):
			run('pacman -S --noconfirm --need lib32-ncurses lib32-libxml2 lib32-zlib lib32-bzip2 lib32-readline lib32-curl')
		else:
			run('pacman -S --noconfirm --need lib64-ncurses lib64-libxml2 lib64-zlib lib64-bzip2 lib64-readline lib64-curl')

		super(init, self).install()
