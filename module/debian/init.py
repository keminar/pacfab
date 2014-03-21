# encoding: utf-8

import conf
from fabric.api import *
from module.common.init import init
class init(init):
	def install(self):
		super(init, self).prepare()
		run('apt-get update -y')
		run('apt-get install -y build-essential')
		run('apt-get install -y libncurses5-dev libxml2-dev zlib1g-dev libbz2-dev libmcrypt-dev libreadline-dev')
		run('apt-get install -y libjpeg-dev libpng-dev libxpm-dev libfreetype6-dev libxslt1-dev libsasl2-dev')
		run('apt-get install -y libcurl4-gnutls-dev libldap2-dev')
		if (utils().bit() == "64"):
			run('''
				ln -sf /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/ && \
				ln -sf /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/ && \
				ln -sf /usr/lib/x86_64-linux-gnu/libssl.so /usr/lib/
			''')
		super(init, self).install()
