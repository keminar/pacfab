# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class mcrypt(base):
	def install(self):
		self.libmcrypt()
		self.download(conf.MCRYPT_URL + '/' + conf.MCRYPT + '.tar.gz')
		self.unzip(conf.MCRYPT)
		# http://stackoverflow.com/questions/6383492/cant-compile-mcrypt-configure-failed-mhash-keygen-in-lmhash-no
		with cd(conf.BASE_DIR + '/dist/src/' + conf.MCRYPT):
			run('''
				export LD_LIBRARY_PATH="''' + conf.INSTALL_DIR + '''/opt/mcrypt/lib:''' + conf.INSTALL_DIR + '''/opt/mhash/lib"; \
				export LDFLAGS="-L''' + conf.INSTALL_DIR + '''/opt/mhash/lib/ -I''' + conf.INSTALL_DIR + '''/opt/mhash/include/"; \
				export CFLAGS="-I''' + conf.INSTALL_DIR + '''/opt/mhash/include/"; \
				./configure --prefix=''' + conf.INSTALL_DIR + '''/opt/mcrypt \
				--with-libmcrypt-prefix='''  + conf.INSTALL_DIR + '''/opt/mcrypt \
				--with-libiconv-prefix=''' + conf.INSTALL_DIR + '''/opt/libiconv \
			''')
			run('make && make install')
		run('touch ' + conf.INSTALL_DIR + '/opt/mcrypt/.install.log')

	def libmcrypt(self):
		self.download(conf.LIBMCRYPT_URL + '/' + conf.LIBMCRYPT + '.tar.gz')
		self.unzip(conf.LIBMCRYPT)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.LIBMCRYPT):
			run('''
				./configure --prefix=''' + conf.INSTALL_DIR + '''/opt/mcrypt \
				--disable-posix-threads
			''')
			run('make && make install')
		with cd(conf.BASE_DIR + '/dist/src/' + conf.LIBMCRYPT + '/libltdl'):
			run('''
				./configure --prefix=''' + conf.INSTALL_DIR + '''/opt/mcrypt \
				--enable-ltdl-install
			''')
			run('make && make install')

	def require(self):
		str = base.require(self)
		return str + ',iconv,mhash'

	def check(self):
		return self.test(conf.INSTALL_DIR + '/opt/mcrypt/.install.log')
