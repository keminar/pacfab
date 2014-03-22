# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class apache(base):
	def install(self):
		self.download(conf.MIRROR + '/apache/' + conf.APACHE + '.tar.gz')
		self.unzip(conf.APACHE)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.APACHE):
			run('''
				./configure  --prefix=''' + conf.INSTALL_DIR + '''/opt/apache \
				--enable-ssl --with-ssl=''' + conf.INSTALL_DIR + '''/opt/ssl \
				--enable-so --enable-rewrite \
				--enable-module=most \
				--with-apr=/usr/local/apr \
				--with-apr-util=/usr/local/apr-util/ \
				--disable-ipv6
			''')
			run('make && make install')
		run('touch ' + conf.INSTALL_DIR + '/opt/apache/.install.log')

	def require(self):
		str = base.require(self)
		return str + ',apr,openssl'

	def check(self):
		return self.test(conf.INSTALL_DIR + '/opt/apache/.install.log')
