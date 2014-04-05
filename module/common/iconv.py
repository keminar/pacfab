# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class iconv(base):
	def install(self):
		self.download(conf.GNU_URL + '/libiconv/' + conf.ICONV + '.tar.gz')
		self.unzip(conf.ICONV)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.ICONV):
			self.patch()
			run('./configure --prefix=' + conf.INSTALL_DIR + '/opt/libiconv --enable-extra-encodings')
			run('make && make install')
		run('touch ' + conf.INSTALL_DIR + '/opt/libiconv/.install.log')

	def check(self):
		return self.test(conf.INSTALL_DIR + '/opt/libiconv/.install.log')

	# libiconv gets undeclared
	# http://forum.z27315.com/topic/15662-%E8%A7%A3%E5%86%B3%E7%BC%96%E8%AF%91libiconv%E6%97%B6%E7%9A%84gets-undeclared-here%E9%94%99%E8%AF%AF/
	def patch(self):
		put(conf.BASE_DIR + '/conf/libiconv/stdio.in.h.patch', conf.BASE_DIR + '/dist/src/' + conf.ICONV + '/srclib/')
		run('patch srclib/stdio.in.h < srclib/stdio.in.h.patch')

