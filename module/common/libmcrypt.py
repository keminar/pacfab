# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class libmcrypt(base):
	def install(self):
		self.download(conf.LIBMCRYPT_URL + '/' + conf.LIBMCRYPT + '.tar.gz')
		self.unzip(conf.LIBMCRYPT)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.LIBMCRYPT):
			run('''
				./configure --prefix=''' + conf.INSTALL_DIR + '''/opt/libmcrypt \
				--disable-posix-threads
			''')
			run('make && make install')
		with cd(conf.BASE_DIR + '/dist/src/' + conf.LIBMCRYPT + '/libltdl'):
			run('''
				./configure --prefix=''' + conf.INSTALL_DIR + '''/opt/libmcrypt \
				--enable-ltdl-install
			''')
			run('make && make install')
		run('touch ' + conf.INSTALL_DIR + '/opt/libmcrypt/.install.log')

	def check(self):
		return self.test(conf.INSTALL_DIR + '/opt/libmcrypt/.install.log')
