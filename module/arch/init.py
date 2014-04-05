# encoding: utf-8

import conf
from fabric.api import *
from core.utils import utils
from module.common.init import init
class init(init):
	def install(self):
		with quiet():
			if (run('grep "/etc/profile.d" /etc/profile') == ""):
				put(conf.BASE_DIR + '/conf/init/profile.tpl', conf.BASE_DIR)
				run('cat ' + conf.BASE_DIR + '/profile.tpl >> /etc/profile')
		run('pacman -S --noconfirm --need base-devel')
		run('pacman -S --noconfirm --need wget')
		run('pacman -S --noconfirm --need libjpeg-turbo libpng libxpm freetype2 libxslt libsasl')
		run('pacman -S --noconfirm --need curl libldap pcre')
		run('pacman -S --noconfirm --need ncurses libxml2 zlib bzip2 readline')

		super(init, self).install()
