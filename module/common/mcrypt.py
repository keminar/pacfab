# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class mcrypt(base):
	def install(self):
		self.download(conf.MCRYPT_URL + '/' + conf.MCRYPT + '.tar.gz')
		self.unzip(conf.MCRYPT)
		# http://stackoverflow.com/questions/6383492/cant-compile-mcrypt-configure-failed-mhash-keygen-in-lmhash-no
		with cd(conf.BASE_DIR + '/dist/src/' + conf.MCRYPT):
			run('''
				export LD_LIBRARY_PATH="''' + conf.INSTALL_DIR + '''/opt/libmcrypt/lib:''' + conf.INSTALL_DIR + '''/opt/mhash/lib"; \
				export LDFLAGS="-L''' + conf.INSTALL_DIR + '''/opt/mhash/lib/ -I''' + conf.INSTALL_DIR + '''/opt/mhash/include/"; \
				export CFLAGS="-I''' + conf.INSTALL_DIR + '''/opt/mhash/include/"; \
				./configure --prefix=''' + conf.INSTALL_DIR + '''/opt/mcrypt \
				--with-libmcrypt-prefix='''  + conf.INSTALL_DIR + '''/opt/libmcrypt \
				--with-libiconv-prefix=''' + conf.INSTALL_DIR + '''/opt/libiconv \
			''')
			run('make && make install')
		run('touch ' + conf.INSTALL_DIR + '/opt/mcrypt/.install.log')

	def require(self):
		return 'iconv,mhash,libmcrypt'

	def check(self):
		return self.test(conf.INSTALL_DIR + '/opt/mcrypt/.install.log')
