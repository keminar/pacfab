# encoding: utf-8

import conf
from fabric.api import *
from core.utils import utils
from module.common.init import init
class init(init):
	def install(self):
		with quiet():
			if (run('grep "/etc/profile.d" /etc/profile') == ""):
				put(conf.BASE_DIR + '/conf/init/profile.tpl', conf.BASE_DIR + '/dist/src')
				run('cat ' + conf.BASE_DIR + '/dist/src/profile.tpl >> /etc/profile')
		run('apt-get update -y')
		run('apt-get install -y build-essential wget')
		run('apt-get install -y libncurses5-dev libxml2-dev zlib1g-dev libbz2-dev libreadline-dev')
		run('apt-get install -y libjpeg-dev libpng-dev libxpm-dev libfreetype6-dev libxslt1-dev libsasl2-dev')
		run('apt-get install -y curl libcurl3 libcurl4-gnutls-dev libldap2-dev libpcre3 libpcre3-dev')
		if (utils().bit() == "64"):
			run('''
				ln -sf /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/ && \
				ln -sf /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/ && \
				ln -sf /usr/lib/x86_64-linux-gnu/libssl.so /usr/lib/
			''')
		super(init, self).install()
