# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class openssl(base):
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
	def check(self):
		with quiet():
			output = run('test -e ' + conf.INSTALL_DIR + '/opt/ssl ;echo $?')
			return output
