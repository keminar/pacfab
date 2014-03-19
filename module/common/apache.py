# encoding: utf-8

import conf
from fabric.api import *
from module.common.base import base
class apache(base):
	def install(self):
		self.download(conf.MIRROR + '/apache/' + conf.APACHE + '.tar.gz')
		self.unzip(conf.APACHE)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.APACHE):
			run('''
				./configure  --prefix=''' + conf.INSTALL_DIR + '''/opt/apache \
				--enable-so --enable-ssl --with-ssl=/usr/local/ssl \
				--enable-rewrite \
				--enable-module=most \
				--with-apr=/usr/local/apr \
				--with-apr-util=/usr/local/apr-util/ \
				--disable-ipv6
			''')
			run('make && make install')

	def require(self):
		str = base.require(self)
		return str + ',apr,openssl'

	def check(self):
		with quiet():
			output = run('test -e ' + conf.INSTALL_DIR + '/opt/apache ;echo $?')
			return output
