# encoding: utf-8

import conf
from fabric.api import *
from module.common.base import base
class openssl(base):
	def install(self):
		self.download(conf.OPENSSL_URL + '/source/' + conf.OPENSSL + '.tar.gz')
		self.unzip(conf.OPENSSL)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.OPENSSL):
			run('''
				./config --prefix=/usr/local --openssldir=/usr/local/ssl &&\
				make && make install
			''')

