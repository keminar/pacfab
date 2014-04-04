# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class openssl(base):
	# -fPIC no-gost
	# http://www.apachelounge.com/viewtopic.php?t=4690
	def install(self):
		self.download(conf.OPENSSL_URL + '/source/' + conf.OPENSSL + '.tar.gz')
		self.unzip(conf.OPENSSL)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.OPENSSL):
			run('''
				./config --prefix=''' + conf.INSTALL_DIR + '''/opt/ssl \
				--openssldir=''' + conf.INSTALL_DIR + '''/opt/ssl \
				-fPIC no-gost no-shared no-zlib
			''')
			run('make && make install')
		run('touch ' + conf.INSTALL_DIR + '/opt/ssl/.install.log')

	def check(self):
		return self.test(conf.INSTALL_DIR + '/opt/ssl/.install.log')
